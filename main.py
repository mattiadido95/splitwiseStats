import numpy as np
import pandas as pd
import utils

df = pd.read_csv(r'data/exportSplitwiseCSV.csv', sep=";")
df = df.dropna()
# df['Data'] = df['Data'].replace(np.nan, "01/01/1900")
# df['Categorie'] = df['Categorie'].replace(np.nan, "nulli")
df["mese"] = df["Data"].apply(lambda x: utils.getMonth(x))
df["anno"] = df["Data"].apply(lambda x: utils.getYear(x))
df.to_csv('data/file_name.csv', index=False, sep=";")
print(df)
