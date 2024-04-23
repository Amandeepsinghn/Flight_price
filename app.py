from flask import Flask,render_template,request
import pandas as pd 
import numpy as np 
from src.pipeline.predict_pipeline import CustomData,PredictionPipeline


application=Flask(__name__)   #intiating the application

app=application


@app.route('/')
def index():
    return render_template('index.html')  # returning the index html 


@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Airline=request.form.get('Airline'),
            Source=request.form.get('Source'),
            Destination=request.form.get('Destination'),
            Total_Stops=request.form.get('Total_stops'),
            Journey_month=request.form.get('Journey_month'),
            Journey_day=request.form.get('Journey_day'),
            Dep_hour=request.form.get('Dep_hour'),
            Dep_minute=request.form.get('Dep_minute'),
            Arv_hour=request.form.get('Arv_hour'),
            Arv_minute=request.form.get("Arv_minute"),
            Total_Duration=request.form.get('Total_duration'),
            Route_count=request.form.get('Route_count')

           )
        
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictionPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)