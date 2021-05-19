import csv


def read_csv(filepath):
    try:
        file_reader = csv.DictReader(open(filepath))
        result = []
        for row in file_reader:
            result.append(row)
        return result
    except FileNotFoundError:
        raise Exception("File not found")
