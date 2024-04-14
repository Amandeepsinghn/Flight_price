import os 
import sys 
from src.logger import logging
from src.exception import Custom_Exception
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import Data_Transformation





@dataclass
class Data_Ingestion_Config:
     # defining path for the raw test and train data
    logging.info('giving path of train,test and raw data')
    train_data_path=os.path.join('artifact','train.csv')
    test_data_path=os.path.join('artifact','test.csv')
    raw_data_path=os.path.join('artifact','raw_data.csv')
    
    
    
class Data_ingestion:
    def __init__(self):
        self.ingestion_config=Data_Ingestion_Config()
        
    def initiate_data_ingestion(self):
        try:
            # reading the file
            logging.info('we are initiating the data ingestion')
            df=pd.read_csv("Notebook/data/flight.csv")
            logging.info('data has been read correctly')
            
            
            # making the directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            logging.info('making the raw file')
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info('converting the raw data into train and test')
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=31)
            
            logging.info('saving train and test data split')
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info('ingestion has been completed')
            
            # it will return the train and test data path
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
            )           
            
        except Exception as e:
            raise Custom_Exception(e,sys)
        
        
        
if __name__=="__main__":
    a=Data_ingestion()
    train,test=a.initiate_data_ingestion()
    
    b=Data_Transformation()
    _,_,c=b.intiate_data_transformation(train,test)
    
    


    