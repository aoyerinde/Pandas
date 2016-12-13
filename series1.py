import pandas as pd


s=pd.Series(list('abcd'))
##prints the entire one dimensional array
print(s)
print('-------------')

##prints the 1D array with specified index
t=pd.Series([2,4,6,8],
index = ['q','w','e','r'])
print(t)
print('-------------')

##prints the value for a specific index
print(t['q'])
print('-------------')

##prints value of multiple indices
print(t[['q','w']])
print('-------------')



