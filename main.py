import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transforamation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
if __name__ =="__main__":
    try:
        logging.info("Starting data ingestion")
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        data_validation_config = DataValidationConfig(training_pipeline_cofig=training_pipeline_config)
        data_valdiation=DataValidation(data_ingestion_artifact,data_validation_config)
        data_validation_artifact= data_valdiation.initiate_data_validation()
        data_transformation_config=DataTransformationConfig(training_pipeline_config)
        data_transformation =DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        
        model_trainer_config =ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
        model_trainer= ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact =model_trainer.initiate_model_trainer()
        print(model_trainer_artifact)
    except Exception as e:
        raise CustomException(e,sys)    