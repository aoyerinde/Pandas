import pandas as pd

df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})


##only the common columns are displayed when merge is used
##left,right,outer,inner respective to sql joins
df4=pd.merge(df1,df3,on='Year',how='left')
df4.set_index('Year',inplace = True,)
print(df4)


df1.set_index('Year',inplace =True)
df3.set_index('Year',inplace=True)
joined=df1.join(df3,how="outer")
print(joined)
