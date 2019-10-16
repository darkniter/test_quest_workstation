import tempfile
import win32api
import win32print
import config
import json


def get_records():
    with open(config.DATA, 'r+', encoding='utf-8') as data_file:
        data_obj = json.load(data_file)
    return data_obj


def print_from_printer():
    print(win32print.GetDefaultPrinter())


if __name__ == "__main__":
    print_from_printer()
