
#load libraries
import pandas as pd
import seaborn as sns

#read data
airbnb = pd.read_csv('data/Newyork_airbnb/AB_NYC_2019.csv')
airbnb.head()

#check price distribution
sns.scatterplot(data = airbnb['price'])

# if condition
opt = 'high'
df = ''
if opt == 'high':
    df = airbnb.loc[airbnb['price']>6000]
	
# add second condition
if opt == 'high':
    df = airbnb.loc[airbnb['price']>6000]
elif opt =='mid': #else
    df = airbnb.loc[(airbnb['price']>1000) & (airbnb['price']<6000)]
	
#add else:
if opt == 'high':
    df = airbnb.loc[airbnb['price']>6000]
elif opt =='mid':
    df = airbnb.loc[(airbnb['price']>1000) & (airbnb['price']<6000)]
else:
    df = airbnb.loc[airbnb['price']<1000]
#check price distribution
sns.scatterplot(data = df['price'])

# ternay operator with 2 conditions
airbnb.loc[airbnb['price']>6000] if opt == 'high' else airbnb.loc[(airbnb['price']>1000) & (airbnb['price']<6000)]

# ternay operator with 3 conditions
df = airbnb.loc[airbnb['price']>6000] if opt == 'high' else airbnb.loc[(airbnb['price']>1000) & (airbnb['price']<6000)]

# check values
df['price']