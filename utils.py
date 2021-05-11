import random
import string
from file_service import create_file, read_file, delete_file, get_metadata

FILE_NAME_LENGTH = 10
LETTERS_DIGITS = string.ascii_letters + string.digits


def generate_name() -> str:
    return ''.join(random.choice(LETTERS_DIGITS) for _ in range(FILE_NAME_LENGTH))


def show_options() -> str:
    choice = input('''
        1. Create file.
        2. Read file.
        3. Delete file
        4. Get meta data.
        5. Exit
        ''')
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


def app():
    while True:
        try:
            choice = show_options()
            if choice == '1':
                content = enter_content()
                create_file(content)
            elif choice == '2':
                filename = enter_filename()
                read_file(filename)
            elif choice == '3':
                filename = enter_filename()
                delete_file(filename)
            elif choice == '4':
                filename = enter_filename()
                get_metadata(filename)
            elif choice == '5':
                break
            else:
                raise InvalidOption
        except InvalidOption:
            print_option_error()
        except FileNotFoundError:
            print_location_error()
