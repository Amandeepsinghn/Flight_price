import sys 
import pandas as pd
from sklearn.model_selection import PredefinedSplit 
from src.exception import Custom_Exception
from src.utils import load_object


class PredictionPipeline:
    def __init__(self):
        pass


    def predict(self,features):
        try:
            model_path='C:/ml_projects/Ml_projects/Flight_price/artifact/model.pkl'
            preprocessor_path='C:/ml_projects/Ml_projects/Flight_price/artifact/preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds

        except Exception as e:
            raise Custom_Exception(e,sys)
        




class CustomData:
    def __init__(self,
                 Airline: str,
                 Source: str,
                 Destination:str,
                 Total_Stops,
                 Journey_month,
                 Journey_day,
                 Dep_hour,
                 Dep_minute,
                 Arv_hour,
                 Arv_minute,
                 Total_Duration,
                 Route_count):
        
        self.Airline=Airline
        self.Source=Source
        self.Destination=Destination
        self.Total_Stops=Total_Stops
        self.Journey_month=Journey_month
        self.Journey_day=Journey_day
        self.Dep_hour=Dep_hour
        self.Dep_minute=Dep_minute
        self.Arv_hour=Arv_hour
        self.Arv_minute=Arv_minute
        self.Total_Duration=Total_Duration
        self.Route_count=Route_count
        
        
    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
                'Airline':[self.Airline],
                'Source':[self.Source],
                'Destination':[self.Destination],
                'Total_Stops':[self.Total_Stops],
                'Journey_month':[self.Journey_month],
                'Journey_day':[self.Journey_day],
                'Dep_hour':[self.Dep_hour],
                'Dep_minute':[self.Dep_minute],
                'Arv_hour':[self.Arv_hour],
                'Arv_minute':[self.Arv_minute],
                'Total_Duration':[self.Total_Duration],
                'Route_count':[self.Route_count]

            }
            
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise Custom_Exception(e,sys)
        