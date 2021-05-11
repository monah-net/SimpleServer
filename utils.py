import random
import string
import os

NAME_LENGTH = 10
DEFAULT_OPTION = 999


def generate_name() -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(NAME_LENGTH))


def show_options() -> int:
    try:
        choice = int(input('''
            1. Create file.
            2. Read file.
            3. Delete file
            4. Get meta data.
            5. Exit
            '''))
    except ValueError:
        print('Invalid option\n')
        choice = DEFAULT_OPTION
    return choice


def enter_content() -> str:
    content = input("Please enter file content or press <Enter> to continue.\n")
    return content


def enter_filename() -> str:
    filename = input("Please enter file name.\n")
    return filename


class InvalidOption(Exception):
    pass


def print_option_error():
    print("Choose anohter option.\n")


def print_location_error():
    print("File not found.\n")