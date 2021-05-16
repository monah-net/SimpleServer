import random
import string

FILE_NAME_LENGTH = 10
LETTERS_DIGITS = string.ascii_letters + string.digits


def generate_name() -> str:
    return ''.join(random.choice(LETTERS_DIGITS) for _ in range(FILE_NAME_LENGTH))


def enter_content() -> str:
    content = input("Please enter file content or press <Enter> to continue.\n")
    return content


class InvalidOption(Exception):
    pass


