import pandas as pd 

df = pd.read_csv('Gapminder.csv',error_bad_lines=False, sep=";")

df.head()
