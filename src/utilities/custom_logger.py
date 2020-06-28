import inspect
import logging
import traceback
from logging import Logger


def custom_logger(log_level=logging.DEBUG) -> Logger:
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger: Logger = logging.getLogger(logger_name)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("automation.log", mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]
