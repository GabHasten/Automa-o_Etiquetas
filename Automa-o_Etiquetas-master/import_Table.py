import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1YA4WqaKb5c7TF8E6CemDyC2Oa0BfWZxmDR4Q8lY5Dnc/export?format=csv'

df = pd.read_csv(url)

print('\n',df.head(),'\n')
