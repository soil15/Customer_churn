from src.logger import logging
from src.exception import custom_exception
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import sys
from dataclasses import dataclass
import os
from src.utils import load_obj, save_obj

@dataclass
class ModelTrainningConfg:
    best_param_path = os.path.join('Artifacts', 'best_params.pkl')
    model_path = os.path.join('Artifacts', 'model.pkl')


class ModelTrainning:

    def __init__(self):

        self.model_trainning_cofg_obj = ModelTrainningConfg()

    def initaite_model_trainning(self, X_train, X_test, y_train, y_test):

        try:

            best_params = load_obj(self.model_trainning_cofg_obj.best_param_path)

            model = XGBClassifier(**best_params)

            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            cm = confusion_matrix(y_test, y_pred)

            save_obj(self.model_trainning_cofg_obj.model_path, model)

            logging.info('************************ Classification report ************************')
            logging.info(classification_report(y_test, y_pred))
            logging.info('***********************************************************************')

        except Exception as e:
            logging.info('Exception raised in model trainning')
            raise custom_exception(e, sys)


if __name__ == '__main__':

    data_ing_obj = DataIngestion()
    train_data_path, test_data_path = data_ing_obj.initiate_data_ingestion()
    data_tra_obj = DataTransformation()
    X_train, X_test, y_train, y_test = data_tra_obj.initiate_data_transformation(train_data_path, test_data_path)
    model_train_obj = ModelTrainning()
    model_train_obj.initaite_model_trainning(X_train, X_test, y_train, y_test)