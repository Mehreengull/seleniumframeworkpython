import logging


class LogGen:
    @staticmethod
    def loggen():
        # Create a logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # Define the log file path
        log_file_path = "./logs/automation.log"

        # Create a file handler
        file_handler = logging.FileHandler(log_file_path)

        # Define the log message format
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        # Set the formatter for the file handler
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        return logger


