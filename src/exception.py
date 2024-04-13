import sys 
from src.logger import logging 



def error__msg_detail(error,error_detail:sys): #define the function to use in class
    _,_,exc_tb=error_detail.exc_info()        # only 3rd parameter is required
    file_name=exc_tb.tb_frame.f_code.co_filename
    
    error_message=f"error found in script {file_name} in line {exc_tb.tb_lineno} and error is {str(error)}"
    
    return error_message


class Custom_Exception(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_message=error__msg_detail(error_msg,error_detail)   # using function class to print the exception occured
        
    
    def __str__(self):   # it will autmatically run the error_msg
        return self.error_message    
    

  
