"""CSV type files read module"""
import csv
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def read_csv(filepath):
    """
    Function read_csv reads data from csv file and returns it's data
    :param filepath: file name with "csv" extension
    :return:list
    """
    try:
        with open(filepath) as f:
            file_reader = csv.DictReader(f)
            return [row for row in file_reader]
    except FileNotFoundError:
        logger.error("File not found. Check file name and continue\n")
        raise FileNotFoundError
