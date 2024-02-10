import os
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
# Modelling
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge,Lasso
# from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from exception import CustomException
from logger import logging
from utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    train_model_file_path=os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training & test test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(), 
                # "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor()
            }

        
            model_report:dict=evaluate_models(X_train=X_train, 
                                  y_train=y_train, 
                                  X_test=X_test, 
                                  y_test=y_test, 
                                  models=models)



            # To get best model score from dict
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            
            best_model = models[best_model_name]
            if best_model_score<0.6:
                raise CustomException("No best Model Found")
            logging.info(f"Best model found.")

            save_object(
                file_path=self.model_trainer_config.train_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            r2_score_ = r2_score(y_test, predicted)
            return r2_score_
        
        except Exception as e:
            raise CustomException(e,sys)

