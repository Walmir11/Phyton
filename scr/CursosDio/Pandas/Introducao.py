import pandas as pd

df = pd.read_excel("Gapminder.csv",error_bad_lines=False, sep=";")

df.head()
