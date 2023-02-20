import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel("regions.xlsx")
df_csv = pd.read_csv("Names.csv", header=None)
df_txt = pd.read_csv("data.txt", delimiter='\t')

df_csv.columns = ['First', 'Last',  'Address', 'City', 'State', 'Area Code']

df_csv.to_excel('modified-CG.xlsx')

print(df_excel)
print(df_txt)
print(df_csv)