from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig
import os
import sys
import numpy as np
import pandas as pd
import pymango
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()
MONGO_USERNAME=os.getenv("MONGO_USERNAME")
MONGO_PASSWORD=os.getenv("MONGO_PASSWORD")

MONGODB_URL=os.getenv("MONGODB_URL").format(
    encoded_username=MONGO_USERNAME,encoded_password=MONGO_PASSWORD)

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise CustomException(e, sys)

    def export_collection_as_dataframe(self):
        try:
          database_name=self.data_ingestion_config.database_name
          collection_name=self.data_ingestion_config.collection_name
          self.mongo_client=pymango.MongoClient(MONGODB_URL)
          collection=self.mongo_client[database_name][collection_name]
          pd.DataFrame(list(collection.find()))
          if "_id" in df.columns:
              df=df.drop(columns=["_id"],axis=1)
          
          df.replace(to_replace="na",value=np.NAN,inplace=True)
          return df
        except Exception as e:
            raise CustomException(e, sys)
    
    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe         
        except Exception as e:
            raise CustomException(e, sys)

    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        try:
            train_set,test_set=train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio,
                random_state=42
            )
            logging.info("Performed train test split")
            train_file_path=self.data_ingestion_config.training_file_path
            test_file_path=self.data_ingestion_config.testing_file_path
            dir_path=os.path.dirname(train_file_path)
            os.makedirs(dir_path,exist_ok=True)
            train_set.to_csv(train_file_path,index=False,header=True)
            test_set.to_csv(test_file_path,index=False,header=True)
            logging.info("Ingested data is splitted into train and test file")
            
        except Exception as e:
            raise CustomException(e, sys)
    def initiate_data_ingestion(self):
        try:
          dataframe=self.export_collection_as_dataframe()
          dataframe=self.export_data_into_feature_store(dataframe=dataframe)
          self.split_data_as_train_test(dataframe=dataframe)
        except Exception as e:
            raise CustomException(e, sys)    
        
