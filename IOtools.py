import pandas as pd

df=pd.read_csv('ZILL-Z77006_3B.csv')
##print(df.tail())
df2=df.head(10)
##print(df)
df2.to_html('sample1.html')
