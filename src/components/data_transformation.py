from src.exception import custom_exception
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import category_encoders as ce
from dataclasses import dataclass
from src.components.data_ingestion import DataIngestion
import sys
import os
from src.utils import save_obj


@dataclass
class DataTransformationConfig:

    columns_to_drop = ['account_length','total_eve_minutes','total_eve_calls','total_night_minutes','total_night_calls']
    label_encoding_cols = ['international_plan', 'voice_mail_plan', 'churn', 'area_code']
    target_encoding_cols = ['state']
    target_col = 'churn'
    pre_proc_obj_path = os.path.join('Artifacts', 'pre_proc_objs')
    num_cols = list()
    cat_cols = list()

class DataTransformation:

    def __init__(self):
        
        self.data_trans_confg = DataTransformationConfig()

    def preprocessing(self, dataframe):

        try:

            pre_processing_objects = {}

            dataframe.drop(self.data_trans_confg.columns_to_drop, axis=1, inplace=True)

            for col in self.data_trans_confg.label_encoding_cols:

                lable_enc_obj = LabelEncoder()
                target_encoder = ce.TargetEncoder()

                dataframe[col] = lable_enc_obj.fit_transform(dataframe[col])
                pre_processing_objects[col] = lable_enc_obj

            for col in self.data_trans_confg.target_encoding_cols:

                dataframe[col] = target_encoder.fit_transform(X=dataframe[col], y=dataframe[self.data_trans_confg.target_col])
                pre_processing_objects[col] = target_encoder

            logging.info('Columns selected : {}'.format(dataframe.columns))

            save_obj(self.data_trans_confg.pre_proc_obj_path, pre_processing_objects)

            logging.info('Preprocessing objects : {}'.format(pre_processing_objects))

            return dataframe

        except Exception as e:
            logging.info('Exception occured at data_transformation/preprocessing')
            raise custom_exception(e, sys)

    def initiate_data_transformation(self, train_data_path, test_data_path):

        try:

            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            # self.data_trans_confg.cat_cols = [col for col in train_df.columns if train_df[col].dtype != 'object']
            # self.data_trans_confg.num_cols = [col for col in train_df.columns if train_df[col].dtype == 'object']
            

            logging.info('values : {}'.format(train_df.iloc[0]))

            train_df = self.preprocessing(train_df)
            test_df = self.preprocessing(test_df)

            X_train = train_df.drop(self.data_trans_confg.target_col, axis=1)
            y_train = train_df[self.data_trans_confg.target_col]

            X_test = test_df.drop(self.data_trans_confg.target_col, axis=1)
            y_test = test_df[self.data_trans_confg.target_col]

            return (X_train, X_test, y_train, y_test)            

        except Exception as e:
            logging.info('Exception raised at data_transformation')
            raise custom_exception(e, sys)


if __name__ == '__main__':

    data_inge_obj = DataIngestion()
    train_data_path, test_data_path = data_inge_obj.initiate_data_ingestion()

    data_tra_obj = DataTransformation()
    X_train, X_test, y_train, y_test = data_tra_obj.initiate_data_transformation(train_data_path, test_data_path)