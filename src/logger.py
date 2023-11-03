import logging
import os
from datetime import datetime

already_setup = False


def setup_logging():
    global already_setup
    if already_setup:
        return
    already_setup = True

    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
    os.makedirs(logs_path, exist_ok=True)

    LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )


# if __name__ == '__main___':
#     logging.info("Logging started")
