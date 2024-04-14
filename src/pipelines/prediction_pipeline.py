import pandas as pd
from src.exception import custom_exception
from src.logger import logging
import sys
from src.components.data_transformation import DataTransformation
from src.components.model_trainning import ModelTrainning
from src.utils import load_obj


class Prediction:

    def __init__(self, 
                 state, 
                 area_code, 
                 international_plan, 
                 voice_mail_plan, 
                 number_vmail_messages, 
                 total_day_minutes, 
                 total_day_calls, 
                 total_day_charge, 
                 total_eve_charge, 
                 total_night_charge, 
                 total_intl_minutes, 
                 total_intl_calls, 
                 total_intl_charge, 
                 number_customer_service_calls):
        
        self.state = state
        self.area_code =  area_code
        self.international_plan =  international_plan
        self.voice_mail_plan = voice_mail_plan
        self.number_vmail_messages = number_vmail_messages
        self.total_day_minutes = total_day_minutes
        self.total_day_calls = total_day_calls
        self.total_day_charge = total_day_charge
        self.total_eve_charge =  total_eve_charge
        self.total_night_charge =  total_night_charge
        self.total_intl_minutes = total_intl_minutes 
        self.total_intl_calls = total_intl_calls
        self.total_intl_charge = total_intl_charge
        self.number_customer_service_calls = number_customer_service_calls


    def get_data(self):

        data_dict = {            
            'state' : self.state,
            'area_code': self.area_code,
            'international_plan': self.international_plan,
            'voice_mail_plan' : self.voice_mail_plan,
            'number_vmail_messages' : self.number_vmail_messages,
            'total_day_minutes' : self.total_day_minutes,
            'total_day_calls' : self.total_day_calls,
            'total_day_charge' : self.total_day_charge,
            'total_eve_charge' : self.total_eve_charge,
            'total_night_charge' : self.total_night_charge,
            'total_intl_minutes' : self.total_intl_minutes,
            'total_intl_calls' : self.total_intl_calls,
            'total_intl_charge' : self.total_intl_charge,
            'number_customer_service_calls' : self.number_customer_service_calls
        }

        data = pd.DataFrame(data_dict, index=[0])

        return data
    
    def get_predictions(self):

        try:

            data_tran_obj = DataTransformation()
            model_train_obj = ModelTrainning()
            label_enc_cols = data_tran_obj.data_trans_confg.label_encoding_cols
            target_enc_cols = data_tran_obj.data_trans_confg.target_encoding_cols
            target_col = data_tran_obj.data_trans_confg.target_col

            pre_proc_obj = load_obj(data_tran_obj.data_trans_confg.pre_proc_obj_path)
            model = load_obj(model_train_obj.model_trainning_cofg_obj.model_path)

            df = self.get_data()

            for col in label_enc_cols:

                if col != target_col:

                    encoder = pre_proc_obj[col]
                    df[col] = encoder.transform(df[col])

            for col in target_enc_cols:

                encoder = pre_proc_obj[col]
                df[col] = encoder.transform(df[col])


            prediction = model.predict(df)

            class_repo = load_obj(model_train_obj.model_trainning_cofg_obj.class_repo_path)

            return (df, prediction, class_repo)
            

        except Exception as e:
            raise custom_exception(e, sys)
