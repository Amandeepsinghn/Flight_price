import os 
from dataclasses import dataclass
from src.exception import Custom_Exception
from src.logger import logging
from src.utils import save_object
from src.utils import evaluate_model
import sys
from sklearn.ensemble import AdaBoostRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from lightgbm import LGBMRegressor
from src.utils import best_model_name
from src.utils import save_object


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifact','model.pkl')
    
class Model_trainer:
    def __init__(self):
        self.trained_model=ModelTrainerConfig()
        
    
    def initaite_model_trainer(self,train_array,test_array):
        try:
            logging.info('splitting the test and train array')
            X_train,y_train,X_test,y_test=(train_array[:,:-1],train_array[:,-1]
                                           ,test_array[:,:-1],test_array[:,-1])
            
            models={
                'Random Forest': RandomForestRegressor(),
                'Decision tree': DecisionTreeRegressor(),
                'Gradient Boositng': GradientBoostingRegressor(),
                'Linear Regression' : LinearRegression(),
                'XGBRegressor': XGBRegressor(),
        
                'AdaBoost Regressor' : AdaBoostRegressor(),
            }
            
            model_report:dict=evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)
            logging.info('model report have been made succesfully')
            
            
            best_model_score=max(sorted(model_report.values()))
            
            best_model_name= list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
            ]
            
            best_model=models[best_model_name]
            logging.info('best model has been found')
            
            if best_model_score<0.6:
                raise Custom_Exception("no best model")
            
            save_object(file_path=self.trained_model.trained_model_file_path,obj=best_model)

            
            predicted=best_model.predict(X_test)
            
            score=r2_score(y_test,predicted)
            
            return score
         
            
        except Exception as e:
            raise Custom_Exception(e,sys)