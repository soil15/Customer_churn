from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainning import ModelTrainning
from src.logger import logging
from src.exception import custom_exception


if __name__ == '__main__':

    data_ing_obj = DataIngestion()
    train_data_path, test_data_path = data_ing_obj.initiate_data_ingestion()
    
    data_trans_obj = DataTransformation()
    X_train, X_test, y_train, y_test = data_trans_obj.initiate_data_transformation(train_data_path=train_data_path, test_data_path=test_data_path)

    modeL_trainning_obj = ModelTrainning()
    modeL_trainning_obj.initaite_model_trainning(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)
    