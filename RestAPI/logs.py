import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
console_logger = logging.StreamHandler()
file_logger = logging.FileHandler(filename="main.log")
console_logger.setFormatter(console_formatter)
file_logger.setFormatter(file_formatter)
logger.addHandler(file_logger)
logger.addHandler(console_logger)
