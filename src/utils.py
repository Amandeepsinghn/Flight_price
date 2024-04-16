import dill
from src.logger import logging
from src.exception import Custom_Exception
import sys
import os
from sklearn.metrics import r2_score
from sklearn.model_selection import RandomizedSearchCV


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
    
    
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise Custom_Exception(e,sys)
    
    
    
def evaluate_model(X_train,y_train,X_test,y_test,models,params):
    try:
        report={}
        logging.info('predicting the model accuracy')
        for i in range(len(models)):
            model=list(models.values())[i] #giving the model name 
            para=params[list(models.keys())[i]]
            
            rs=RandomizedSearchCV(model,para,cv=5,n_jobs=-1,verbose=1)
            rs.fit(X_train,y_train)
            
            
            model.set_params(**rs.best_params_)
            model.fit(X_train,y_train)
            # string the prediction of model accuracy in test and training dataset 
            y_test_pred=model.predict(X_test)
            
            y_train_pred=model.predict(X_train)
            
            test_accuracy=r2_score(y_test,y_test_pred)
            
            train_accuracy=r2_score(y_train,y_train_pred)
            
            report[list(models.keys())[i]]=test_accuracy
            logging.info('checking the accuracy of every model')
            
        return report
        
    except Exception as e:
        raise Custom_Exception(e,sys)
    

def best_model_name(dictionary,value):
    return [key for key,val in dictionary.items() if val==value]

