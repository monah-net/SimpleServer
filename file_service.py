import os
import utils
import logging
from typing import Dict


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
        logging.info(f'File {filename} was created in {os.getcwd()} directory.')
        return filename
    except FileNotFoundError:
        logging.error('File wasn\'t created.')


def read_file(filename: str) -> str:
    """
    Read content of the file.

    Args:
        filename: name of the file with extension.
    Returns:
        content of the file.
    Raises:
        FileNotFoundError: if defined file doesn't exist.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        logging.error('Cant read file. File wasn\'t not found.')


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
        logging.info(f'File {filename} was deleted')
    except FileNotFoundError:
        logging.error('Cant delete file. File wasn\'t not found.')


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
        logging.error('Cant get metadata. File wasn\'t not found.')

