import pickle
import os
import sys
from src.logger import logging
from src.exception import custom_exception


def save_obj(file_path, obj):

    try:

        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:

        logging.info('Exception rasied durinf saving object')
        raise custom_exception(sys, e)


def load_obj(file_path):

    try:

        dit_path = os.path.dirname(file_path)

        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging.info('Exception occured while loading object')
        raise custom_exception(e, sys)