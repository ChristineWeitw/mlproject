import os
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer   # handling missing values 
from sklearn.pipeline import Pipeline
from exception import CustomException
from logger import logging
from utils import save_object

@dataclass  
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsble or data transformation
        '''

        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            # pipelines
            num_pipeline = Pipeline(

                steps=[
                    ("imputer", SimpleImputer(strategy="median")),  # Deal with numeric Missing values with median
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )


            cat_pipeline = Pipeline(

                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),  # Deal with categorical Missing values with most frequent value
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            logging.info("Pipelines creation Completed")


            preprocessor = ColumnTransformer(
                    [
                        ("num_pipeline", num_pipeline, numerical_columns),
                        ("cat_pipeline", cat_pipeline, categorical_columns),        
                    ]
                )
            
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train & test data completed")
        
        # Create preprocessor instance
            preprocessing_obj = self.get_data_transformer_object()
        # Split Features & target Label
            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]
            logging.info("Split Features & target Label completed")

        # fit transformation 
            transformed_input_feature_train_df = preprocessing_obj.fit_transform(input_feature_train_df)
            transformed_input_feature_test_df = preprocessing_obj.transform(input_feature_test_df)
            logging.info("preprocessor fit_transform() completed")
        # Combine transformed features columns with original Target values
            train_arr = np.c_[
                transformed_input_feature_train_df, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                transformed_input_feature_test_df, np.array(target_feature_test_df)
            ]
            logging.info("Combine transformed Features columns with original Target values completed")
        # Save object
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            logging.info("Save object completed")
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)





# feature engineering - numeric/ categorica columns
# Input - raw df; Output - after .fit_transform()

# @dataclass  # when a class only has variales; otherwise use __init__ when there's methods in class
# class DataTransformationConfig:
#     preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")
#     train_df: pd.read_csv('artifacts/train.csv')
#     test_df: pd.read_csv('artifacts/test.csv')
#     raw_df: pd.read_csv('artifacts/raw.csv')

# class DataTransformation:
#     def __init__(self):
#         self.data_transformation_config = DataTransformationConfig()
#         self.num_features = self.transformation_config.raw_df.select_dtypes(exclude="object").columns
#         self.cat_features = self.transformation_config.raw_df.select_dtypes(include="object").columns
#         self.numeric_transformer = StandardScaler()
#         self.oh_transformer = OneHotEncoder()
#         self.preprocessor = ColumnTransformer(
#                     [
#                         ("OneHotEncoder", self.oh_transformer, self.cat_features),
#                         ("StandardScaler", self.numeric_transformer, self.num_features),        
#                     ]
# )
#     def get_data_transformer_object(self): 
#         try:
#             pass
#         except:
#             pass
#         return self.preprocessor.fit_transform(df)



