from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np


app = FastAPI()


model = joblib.load("iris_model.pkl")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(data: IrisInput):

    input_data = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    prediction = model.predict(input_data)

    flower_names = ["Setosa", "Versicolor", "Virginica"]

    result = flower_names[prediction[0]]

    return {
        "prediction": result
    }