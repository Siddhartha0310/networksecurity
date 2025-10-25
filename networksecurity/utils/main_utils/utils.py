import yaml
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
import os,sys
import dill
import pickle
import pandas as pd
import numpy as np
def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path) as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e,sys) 
    

def write_yaml_file(file_path:str,content:object,replace:bool=False)->None:
    try:
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Created directory: {dir_path}")
        
        if os.path.exists(file_path):
            if replace:
                os.remove(file_path)
                logging.info(f"Removed existing file: {file_path}")
            
        
        with open(file_path, "w") as file: 
            yaml.dump(content, file, default_flow_style=False, sort_keys=False)  # Optional: Pretty-print YAML
        logging.info(f"Successfully wrote YAML to: {file_path}")
    except Exception as e:
              raise CustomException(e,sys)

def save_nump_array_data(file_path:str, array:np.array):
     try:
          dir_path=os.path.dirname(file_path)
          os.makedirs(dir_path,exist_ok=True)
          with open(file_path,"wb")as file_obj:
               np.save(file_obj,array)
    
     except Exception as e:
          raise CustomException(e,sys) from e                   
     
def save_object(file_path:str,obj:object)->None:
     try:
          os.makedirs(os.path.dirname(file_path),exist_ok=True)
          with open(file_path,"wb")as file_obj:
               pickle.dump(obj,file_obj)

     except Exception as e:
          raise CustomException(e,sys) from e          
