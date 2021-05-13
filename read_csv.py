import pandas as pd


def read_csv(file):
    return pd.read_csv(file, delimiter=';')


def read_excel(file):
    return pd.read_excel(file, sheet_name='Input')


def read_json(file):
    return pd.read_json(file)
