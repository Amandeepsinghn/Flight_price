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
            
            params={
                "Decision tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "Gradient Boositng":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "XGBRegressor":{
                    'n_estimators': [100, 200, 300],
                    'learning_rate': [0.01, 0.05, 0.1, 0.2],
                    'max_depth': [3, 4, 5, 6],
                    'min_child_weight': [1, 2, 3, 4],
                    'gamma': [0, 0.1, 0.2, 0.3],
                    'subsample': [0.6, 0.7, 0.8, 0.9],
                    'colsample_bytree': [0.6, 0.7, 0.8, 0.9],
                    'reg_alpha': [0, 0.1, 0.5, 1],
                    'reg_lambda': [0, 0.1, 0.5, 1],
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }              
            }
            
            
            
            
            
            model_report:dict=evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models,params=params)
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
        
        