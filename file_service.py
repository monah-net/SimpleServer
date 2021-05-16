import os
import utils
import logging


def create_file(file_extension, content=''):
    try:
        filename = f'{utils.generate_name()}.{file_extension}'
        with open(filename, 'w') as file:
            file.write(content)
        logging.info(f'File {filename} was created in {os.getcwd()} directory.')
        return filename
    except FileNotFoundError:
        logging.error('File wasn\'t created.')


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        logging.error('Cant read file. File wasn\'t not found.')


def delete_file(filename):
    try:
        os.remove(filename)
        logging.info(f'File {filename} was deleted')
    except FileNotFoundError:
        logging.error('Cant delete file. File wasn\'t not found.')


def get_metadata(filename):
    try:
        metadata = {'file_name': filename, 'location': os.path.abspath(filename), 'size': os.path.getsize(filename)}
        return metadata
    except FileNotFoundError:
        logging.error('Cant get metadata. File wasn\'t not found.')
