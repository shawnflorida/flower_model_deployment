from fastapi import FastAPI
import joblib
import numpy as np 

model = joblib.load('app/model.joblib')

app= FastAPI()

@app.get('/')
def index():
    return {'message': 'This is the homepage of testing for API for credit scoring from Easycall'}

flower_names = np.array(['setosa', 'versicolor', 'virginica'])

@app.post('/predict') 
def predict(data: dict):
    """
    Predict the class of a flower based on input features.
    
    Args:
        data (dict): A dictionary containing the input features under the key 'features'.
    
    Sample:
        {"features": [5.1, 3.5, 1.4, 0.2]}
        
    Returns:
        dict: A dictionary containing the prediction and the flower names.
            - 'prediction' (str): The predicted class name of the flower.
            - 'flower_names' (list): The list of all possible flower names.
    """
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = flower_names[prediction][0]
    return {'prediction': class_name, 'flower_names': flower_names.tolist()}

