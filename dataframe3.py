import pandas as pd
ob=pd.Series(['blue','purple','red'],index=[0,2,4])

##prints all the values in ob
print(ob)

##prints the values with index from 0 to 4
print(ob.reindex(range(4)))

##fills the columns with values NaN as black
print(ob.reindex(range(5),fill_value='black'))

##fills the columns with NaN with the previous column
print(ob.reindex(range(5),method='ffill'))
