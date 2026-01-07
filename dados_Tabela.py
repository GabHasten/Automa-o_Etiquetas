import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1YA4WqaKb5c7TF8E6CemDyC2Oa0BfWZxmDR4Q8lY5Dnc/export?format=csv'


def carregar_dados():
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip()
    return df




