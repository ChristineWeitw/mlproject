import logging
import os
from datetime import datetime

# Generate a unique log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Correctly set up the logs directory path (assuming correction to the original logic)
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# Ensure the logs directory exists, create it if it doesn't
os.makedirs(logs_path, exist_ok=True)

# Specify the full path for the log file within the logs directory
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# Configure the basic settings for the logging system
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level = logging.INFO,
    )

