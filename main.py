#! /usr/bin/env python3
from file_service import create_file, read_file, delete_file, get_metadata
from utils import InvalidOption
import argparse
import logging


def commandline_parser() -> argparse.ArgumentParser:
    """
    Parse arguments from command line

    Returns:
        arguments from command line
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('action', type=str, help='Action')
    parser.add_argument('-fn', '--file_name', type=str, help='File name')
    parser.add_argument('-fe', '--file_extension', type=str, default='pkl', help='File extension')

    return parser


def app() -> None:
    """
    Run the program.

    Raises:
         InvalidOption: if necessary arguments weren't specified
         FileNotFoundError: if defined file wasn't found
    """
    args = commandline_parser().parse_args()
    try:
        choice = args.action
        if choice == 'create':
            content = input('Enter file content or press <Enter> to continue')
            create_file(args.file_extension, content)
        elif choice == 'read':
            if args.file_name is None:
                raise InvalidOption
            read_file(args.file_name)
        elif choice == 'delete':
            if args.file_name is None:
                raise InvalidOption
            print(args.file_name)
            delete_file(args.file_name)
        elif choice == 'metadata':
            if args.file_name is None:
                raise InvalidOption
            get_metadata(args.file_name)
        else:
            raise InvalidOption
    except InvalidOption:
        logging.error('Invalid option is chosen.')
    except FileNotFoundError:
        logging.error('File is not found.')


if __name__ == '__main__':
    app()
