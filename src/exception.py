import sys
from src.logger import logging


def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = 'Error Occured in Python Script name [{}] line number[{}] error message [{}]'.format(file_name, exc_tb.tb_lineno, 
                                                                                                         str(error))
    return error_message


class custom_exception(Exception):
    
    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail=error_detail)
        # self.error_type = type(error)
        # _,_, exc_tb = error_detail.exc_info()
        # self.file_name = exc_tb.tb_frame.f_code.co_filename
        # self.line_number = exc_tb.tb_lineno

    def __str__(self):

        # self.error_messgae = 'Error Occured in Python Script name [{}] line number[{}] error message [{}]'.format(self.file_name, self.line_number, self.error_type)
        return self.error_message   


if __name__ == '__main__':
    logging.info('Logging has Started')

    try:
        a = 1/0
    except Exception as e:
        logging.info('Exception occured in exception.py')
        raise custom_exception(e, sys)

