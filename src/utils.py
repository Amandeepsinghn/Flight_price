import dill
from src.logger import logging
from src.exception import Custom_Exception
import sys
import os


def save_object(file_path,obj):
    try:
        # name the directory
        dir_path=os.path.dirname(file_path)
        # make directory 
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file:
            dill.dump(obj,file)
        
        
    except Exception as e:
        raise Custom_Exception(e,sys)