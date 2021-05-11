import os
import utils


def create_file(content=''):
    filename = utils.generate_name() + '.txt'
    with open(filename, 'w') as file:
        file.write(content)
    print(f'File {filename} was created in {os.getcwd()} directory.')


def read_file(filename) -> str:
    with open(filename, 'r') as file:
        content = file.read()
    print(content)


def delete_file(filename):
    os.remove(filename)
    print(f'file {filename} was deleted')


def get_metadata(filename) -> dict:
    metadata = {'file_name': filename, 'location': os.path.abspath(filename), 'size': os.path.getsize(filename)}
    for key, value in metadata.items():
        print(key, ': ', value)
