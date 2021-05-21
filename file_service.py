import os
import utils
from utils import logger, UnknownFileExtension
from typing import Dict
import csv
import openpyxl as op
import json


def read_csv_file(filepath):
    """
    Read data from CSV file.

    Args:
        filepath: file name with "csv" extension
    Returns:
        list: content of the file.
    Raises:
        FileNotFoundError: if file doesn't exist.
    """
    try:
        with open(filepath) as f:
            file_reader = csv.DictReader(f)
            return [row for row in file_reader]
    except FileNotFoundError:
        logger.error("File not found. Check file name and continue\n")
        raise FileNotFoundError


def read_excel_file(filename):
    """
    Read data from EXCEL file.

    Args:
        filename: file name with "xls" extension
    Returns:
        list: content of the file.
    Raises:
        FileNotFoundError: if file doesn't exist.
    """
    open_file = None
    try:
        open_file = op.load_workbook(filename=filename, read_only=True)
        sheet = open_file.active
        sheet = open_file.worksheets[sheet]
        return [[cell.value for cell in row] for row in sheet.iter_rows()]
    except FileNotFoundError:
        logger.error("File not found. Check file name and continue\n")
    finally:
        if open_file is not None:
            open_file.close()


def read_json_file(filename):
    """
    Read data from json file.

    Args:
        filename: file name with "json" extension
    Returns:
        dict: content of the file.
    Raises:
        FileNotFoundError: if file doesn't exist.
    """
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("File not found. Check file name and continue\n")


def create_file(file_extension: str, content='') -> str:
    """
    Create file with random name and definite extension.

    Args:
        file_extension: extension of the created file.
        content: content of the file (default: empty string).
    Returns:
        file name with extension.
    Raises:
        FileNotFoundError: if file wasn't created.
    """
    try:
        filename = f'{utils.generate_name()}.{file_extension}'
        with open(filename, 'w') as file:
            file.write(content)
        logger.info(f'File {filename} was created in {os.getcwd()} directory.')
        return filename
    except FileNotFoundError:
        logger.error('File wasn\'t created.')


def read_file(filename: str):
    """
    Read content from the file.

    Args:
        filename: name of the file with extension.
    Returns:
        content of the file.
    Raises:
        FileNotFoundError: if defined file doesn't exist.
    """
    try:
        file_extension = os.path.splitext(filename)[1]
        if file_extension == '.csv':
            return read_csv_file(filename)
        if file_extension == '.xlsx':
            return read_excel_file(filename)
        if file_extension == '.json':
            return read_json_file(filename)
        raise UnknownFileExtension
    except FileNotFoundError:
        logger.error('Cant read file. File wasn\'t not found.')
    except UnknownFileExtension:
        logger.error('Cant read file. Unknown file extension.')


def delete_file(filename: str) -> None:
    """
     Delete defined file.

     Args:
         filename: name of the file with extension.
     Raises:
         FileNotFoundError: if the defined file doesn't exist.
     """
    try:
        os.remove(filename)
        logger.info(f'File {filename} was deleted')
    except FileNotFoundError:
        logger.error('Cant delete file. File wasn\'t not found.')


def get_metadata(filename: str) -> Dict[str, str]:
    """
    Get metadata of the file.

     Args:
         filename: name of the file with extension.
     Raises:
         FileNotFoundError: if the defined file doesn't exist.
     """
    try:
        metadata = {'file_name': filename, 'location': os.path.abspath(filename), 'size': os.path.getsize(filename)}
        return metadata
    except FileNotFoundError:
        logger.error('Cant get metadata. File wasn\'t not found.')

