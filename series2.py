import pandas as pd

t=pd.Series([2,4,6,8],
index = ['q','w','e','r'])

print(t)
print("----------")

print(t[t>5])
print("----------")

print('NumPy operations')
print(t>4)
print("----------")
print(t*3)

sdata={'a':1,'c':3,'b':2}
s=pd.Series(sdata,list('abcd'))
sdata2={'d':10,'c':30,'b':20}
s2=pd.Series(sdata2,list('abcd'))

print('pandas will acomodate incomplete data')
print("----------")
print(s)

print('Data is automatically aligned')
print("----------")
print(s2*s)



    



