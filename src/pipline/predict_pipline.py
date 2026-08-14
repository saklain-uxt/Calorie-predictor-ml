import sys
import os
import pandas as pd

from src.exception import CustomException
from src.utiles import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            print("Before Loading")

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            print("After Loading")

            data_scaled = preprocessor.transform(features)

            preds = model.predict(data_scaled)

            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(
        self,
        gender,
        age,
        height,
        weight,
        duration,
        heart_rate,
        body_temp
    ):
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.duration = duration
        self.heart_rate = heart_rate
        self.body_temp = body_temp

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Gender": [self.gender],
                "Age": [self.age],
                "Height": [self.height],
                "Weight": [self.weight],
                "Duration": [self.duration],
                "Heart_Rate": [self.heart_rate],
                "Body_Temp": [self.body_temp]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)