import sys 
from dataclasses import dataclass

import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,MinMaxScaler

from src.logger import logging
from src.exception import Custom_Exception
import os 
from src.utils import save_object

@dataclass
class Data_Transformation_config:
    data_transorformation=os.path.join('artifact','preprocessor.pkl')
    
class Data_Transformation:
    def __init__(self):
        self.transformation=Data_Transformation_config()
        
    def get_data_transformed(self):
        logging.info('making data transformation pickle file')
        
        try:
            logging.info('making numerical and categorical columns')
            numerical_cols=['Total_Stops','Journey_month','Journey_day','Dep_hour','Dep_minute','Arv_hour','Arv_minute','Total_Duration','Route_count']
            categorical_cols=['Airline','Source','Destination']
            
            
            categircal_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('one hot encoding',OneHotEncoder())
                ]
            )
            
            numerical_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='mean')),
                    ('scaling',MinMaxScaler())
                ]
            )
            
            logging.info('numerical and categorical pipeline have been made')
            
            preprocessor=ColumnTransformer( # this part intiate the scaling and imputer
                [
                    ("num_pipeline",numerical_pipeline,numerical_cols),
                    ('cat_pipeline',categircal_pipeline,categorical_cols)
                ]
            )
            
            logging.info('transformation has been completed')
            return preprocessor
            
        except Exception as e:
            raise Custom_Exception(e,sys)
        
    
    def intiate_data_transformation(self,train_path,test_path):
        try:
            logging.info('intitating the data_transfromation')
            
            target_cols=['Price']
            
            train_ds=pd.read_csv(train_path)
            test_ds=pd.read_csv(test_path)
            
            logging.info('test and train csv have been read successfully')
            
            preprocessor_obj=self.get_data_transformed()
            
            train_input_feat=train_ds.drop(target_cols,axis=1)
            train_target_feat=train_ds[target_cols]
            logging.info('train split has been completed')
            
            test_input_feat=test_ds.drop(target_cols,axis=1)
            test_target_feat=test_ds[target_cols]
            logging.info('test data has been splittted')
            
            train_feat_transformed=preprocessor_obj.fit_transform(train_input_feat)
            test_feat_transformed=preprocessor_obj.transform(test_input_feat)
            logging.info('preprocessor has been applied to train and test indepedent feature')
            
            logging.info('concating trained array and target array')
            train_arr=np.c_[train_feat_transformed,np.array(train_target_feat)]
            test_arr=np.c_[test_feat_transformed,np.array(test_target_feat)]
            
            logging.info('data transformation has been completed')
            
            save_object(file_path=self.transformation.data_transorformation,obj=preprocessor_obj)
            logging.info('pickle has been saved')
            
            return(
                train_arr,
                test_arr,
                self.transformation.data_transorformation
            )
            
                
        except Exception as e:
            raise Custom_Exception(e,sys)