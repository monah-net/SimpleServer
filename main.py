#! /usr/bin/env python3
from file_service import create_file, read_file, delete_file, get_metadata
from utils import *

if __name__ == '__main__':
    flag = True
    while flag:
        try:
            choice = show_options()
            if choice == 1:
                content = enter_content()
                create_file(content)
            elif choice == 2:
                filename = enter_filename()
                read_file(filename)
            elif choice == 3:
                filename = enter_filename()
                delete_file(filename)
            elif choice == 4:
                filename = enter_filename()
                get_metadata(filename)
            elif choice == 5:
                flag = False
            else:
                raise InvalidOption
        except InvalidOption:
            print_option_error()
            continue
        except FileNotFoundError:
            print_location_error()
            continue










