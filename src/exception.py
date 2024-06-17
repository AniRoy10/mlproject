import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):    #sys knows the error_details , it has it
    _,_,exc_tb=error_detail.exc_info()              # we are not interseted in first two terms
    file_name=exc_tb.tb_frame.f_code.co_filename    #as per python exception handling doucmentation , thus we can get filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))         #error message

    return error_message

    

class CustomException(Exception):           #inheriting parent exception
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)                 #inheriting __init__ from Exception
        self.error_message=error_message_detail(error_message,error_detail=error_detail)  #we are calling the function from error message
    
    def __str__(self):
        return self.error_message
    

#for testing 
#if __name__=="__main__":
#    try:
#        a=1/0
#    except Exception as e:
#        logging.info("Divide by zero")
#    raise  CustomException(e,sys)   