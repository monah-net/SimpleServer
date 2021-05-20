import csv
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def read_csv(filepath):
    try:
        file_reader = csv.DictReader(open(filepath))
        result = []
        for row in file_reader:
            result.append(row)
        return result
    except FileNotFoundError:
        logger.error("File not found. Check file name and continue\n")
