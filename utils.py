import random
import string
import logging


FILE_NAME_LENGTH = 10
LETTERS_DIGITS = string.ascii_letters + string.digits


def generate_name() -> str:
    """
    Generate random name of the file composed of letters and digits.

    Returns:
        File name.
    """
    return ''.join(random.choice(LETTERS_DIGITS) for _ in range(FILE_NAME_LENGTH))


def enter_content() -> str:
    """
    Show message to input file content.

    Returns:
         file content
    """
    content = input("Please enter file content or press <Enter> to continue.\n")
    return content


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class InvalidOption(Exception):
    pass


class UnknownFileExtension(Exception):
    pass


class LostDBConnection(Exception):
    pass
