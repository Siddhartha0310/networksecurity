import os
import sys
import json
from urllib.parse import quote_plus
from dotenv import load_dotenv
import pymongo
import certifi
ca = certifi.where()
import pandas as pd
import numpy as np
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging

load_dotenv()

user = quote_plus(os.getenv("MONGO_USERNAME"))
password = quote_plus(os.getenv("MONGO_PASSWORD"))
MONGODB_URL = os.getenv("MONGODB_URL").format(
    encoded_username=user, encoded_password=password
)

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)

    def cv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e, sys)
         
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database_name = database
            self.collection_name = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(MONGODB_URL)
            self.database = self.mongo_client[self.database_name]
            self.collection = self.database[self.collection_name]
            self.collection.insert_many(self.records)
            return f"Data Inserted Successfully {len(self.records)}"
        except Exception as e:
            raise CustomException(e, sys)
              
if __name__=="__main__":
        FILE_PATH = "D:/project/NetworkSecurity/Network_DATA/phisingData.csv"
        DATABASE="Siddharth"
        Collection="NetworkData"
        networkobj = NetworkDataExtract()
        records=networkobj.cv_to_json_convertor(file_path=FILE_PATH)
        no_of_records = networkobj.insert_data_mongodb(records,DATABASE,Collection)

