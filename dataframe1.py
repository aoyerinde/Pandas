import pandas as pd
data={'state':['FL','FL','GA','GA','GA'],
        'year':[2010, 2011, 2008, 2010, 2011],
        'pop':[18.8, 19.1, 9.7, 9.7,9.8]}
frame=pd.DataFrame(data)
print(frame)
print('------------')

##displays a single comumn
print(frame[['state','year']])
print('------------------')

##new column added
frame['other']='NaN'
print(frame)
