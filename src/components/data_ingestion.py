from src.exception import custom_exception
from src.logger import logging
from dataclasses import dataclass
import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:

    train_data_path = os.path.join('Artifacts', 'train.csv')
    test_data_path  = os.path.join('Artifacts', 'test.csv')


class DataIngestion:

    def __init__(self):
        self.data_confg_obj = DataIngestionConfig()
    
    def initiate_data_ingestion(self):

        try:

            df = pd.read_csv(os.path.join('data', 'raw_data.csv'))
            logging.info('Data read successfully................')

            df.drop('Unnamed: 0', axis=1, inplace=True)
            df.dropna(inplace=True)
            
            train_data, test_data = train_test_split(df, test_size=0.3, random_state=15)

            os.makedirs(os.path.dirname(self.data_confg_obj.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_confg_obj.test_data_path), exist_ok=True)

            train_data.to_csv(self.data_confg_obj.train_data_path, index=False)
            logging.info('Saved train data to {}'.format(self.data_confg_obj.train_data_path))

            test_data.to_csv(self.data_confg_obj.test_data_path, index=False)
            logging.info('Saved test data to {}'.format(self.data_confg_obj.test_data_path))

            logging.info('Data Ingestion Compelete......................')
            return (self.data_confg_obj.train_data_path, self.data_confg_obj.test_data_path)

        except Exception as e:

            logging.info('Exception Occured at Data Ingestion')
            raise custom_exception(e, sys)
        

if __name__ == '__main__':

    data_ing_obj = DataIngestion()
    data_ing_obj.initiate_data_ingestion()