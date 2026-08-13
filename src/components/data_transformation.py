
import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
from src.utiles import save_object

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


@dataclass
class datatransformConfig:
    preprocessor_obj_file_path = os.path.join(
        "artifacts", "preprocessor.pkl"
    )


class datatransform:

    def __init__(self):
        self.datatransfer_config = datatransformConfig()

    def get_data_transformer_object(self):

        try:

            numerical_column = [
                "Age",
                "Height",
                "Weight",
                "Duration",
                "Heart_Rate",
                "Body_Temp"
            ]

            categorical_column = ["Gender"]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehotencoder", OneHotEncoder(handle_unknown="ignore"))
                ]
            )

            logging.info(
                f"Categorical columns: {categorical_column}"
            )

            logging.info(
                f"Numerical columns: {numerical_column}"
            )

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_column),
                    ("cat_pipeline", cat_pipeline, categorical_column)
                ]
            )

            logging.info("Preprocessor object evaluated")

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):

        try:

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "Calories"

            # Training data
            input_feature_train_df = train_df.drop(
                target_column_name,
                axis=1
            )

            target_feature_train_df = train_df[
                target_column_name
            ]

            # Testing data
            input_feature_test_df = test_df.drop(
                target_column_name,
                axis=1
            )

            target_feature_test_df = test_df[
                target_column_name
            ]

            logging.info(
                "Applying preprocessing object on training "
                "and testing dataframe."
            )

            # Fit on training data
            input_feature_train_arr = preprocessing_obj.fit_transform(
                input_feature_train_df
            )

            # Only transform test data
            input_feature_test_arr = preprocessing_obj.transform(
                input_feature_test_df
            )

            # Combine features + target
            train_arr = np.c_[
                input_feature_train_arr,
                target_feature_train_df
            ]

            test_arr = np.c_[
                input_feature_test_arr,
                target_feature_test_df
            ]

            logging.info("Saved preprocessing object.")

            save_object(
                file_path=self.datatransfer_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.datatransfer_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)