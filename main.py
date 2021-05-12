import uvicorn
from fastapi import FastAPI
import pickle
import os
import pandas as pd
import numpy as np
from pydantic import BaseModel
from sklearn.ensemble import RandomForestRegressor

app = FastAPI()


# Load model
pickle_file_open = open("Regressoion.pkl","rb") # open pickle file in read mode
model = pickle.load(pickle_file_open) # to load the pickle file

# loading dataset with userId
Data_crop = pd.read_csv("AgrcultureDataset.csv")

@app.get('/')
def home():
    return "Welcome All! open FastAPI and input these values in the Post method: EXP - Crop_Year=2000 and you will get CPI- Crop Productivity Index"


@app.post('/predict')
def predict_Crop_yield(Crop_Year:'int'):
    # print(data)
    #Crop_Year = data['Crop_Year']
    #CPI = data['CPI']
    #print(model.predict(CPI))
    result = model.predict(np.array(Crop_Year).reshape(-1,1))
    return (f"The predicted CPI(Crop Productivity Index) is {result}")
    # print(result)


if __name__=="__main__":
    #port = int(os.environ.get("PORT",8000))
    uvicorn.run(app, host='127.0.0.1', port=5000)