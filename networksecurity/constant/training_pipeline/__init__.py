import os
import sys
import numpy as np

DATA_INGESTION_COLLECTION_NAME="NetworkData"
DATA_INGESTION_DATABASE_NAME="Siddharth"
DATA_INGESTION_DIR_NAME="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR="feature_store"
DATA_INGESTION_INGESTED_DIR="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION=0.2

"Defining constatans for trianing pipeline"
TARGET_COLUMN="Result"
PIPELINE_NAME="NetworkSecurity"
ARTIFACT_DIR="Artifacts"
FILE_NAME ="phisingData.csv"

TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"