import os
import sys

# Add the parent directory to sys.path to find the exception module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exception import CustomException
from logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Data input ex. save training_path, train_data, test_data, raw data etc
@dataclass  # when a class only has variales; otherwise use __init__ when there's methods in class
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")  # later on, data ingestion will save the train.csv in this particular path
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):  # read data from db
        logging.info("Entered the data ingestion method or component")
        try:
             df = pd.read_csv('notebook/data/stud.csv')
             logging.info('Read the dataset as df')

            # train data
             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)   # os.path.dirname - get the dir name
             
             # raw data
             df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

             logging.info("Train test split initaited")
             train_set, test_set = train_test_split(df, test_size=0.2, random_state=17)

             train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
             test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
             logging.info("Ingestion of the data is completed")
             
             return (self.ingestion_config.train_data_path,
                     self.ingestion_config.test_data_path, 
                     )
        except Exception as e:
            raise CustomException(e, sys)

if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()