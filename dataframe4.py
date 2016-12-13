import pandas as pd
pop_data={'FL':{2010:18.8, 2011:19.1},
          'GA':{2008:9.7, 2010:9.7, 2011:9.8}}
pop=pd.DataFrame(pop_data)
print(pop)
print('----------')

##calculating sum and mean for the data frames
print(pop.sum())
pop.mean()
print(pop.describe())

##Boolean Indexing
print(pop <9.8)

pop[pop<9.8]=0
print(pop)
