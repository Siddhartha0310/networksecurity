import logging
import os
from datetime import datetime

LOG_DIR_NAME = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
logs_path = os.path.join(os.getcwd(), "logs", LOG_DIR_NAME)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_NAME = f"{LOG_DIR_NAME}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d: %(levelname)s: %(message)s",
    level=logging.INFO
)