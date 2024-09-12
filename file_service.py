import os
import random
import string

FILE_NAME_LENGTH = 10
LETTERS_DIGITS = string.ascii_letters + string.digits


def create_file(content=''):
    try:
        filename = f'{generate_name()} .txt'
        with open(filename, 'w') as file:
            file.write(content)
        print(f'File {filename} was created in {os.getcwd()} directory.')
        return filename
    except FileNotFoundError:
        print_location_error()


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print_location_error()


def delete_file(filename):
    try:
        os.remove(filename)
        return f'file {filename} was deleted'
    except FileNotFoundError:
        print_location_error()


def get_metadata(filename):
    try:
        metadata = {'file_name': filename, 'location': os.path.abspath(filename), 'size': os.path.getsize(filename)}
        return metadata
    except FileNotFoundError:
        print_location_error()


def print_location_error():
    print("File not found.\n")


def generate_name() -> str:
    return ''.join(random.choice(LETTERS_DIGITS) for _ in range(FILE_NAME_LENGTH))
