# load libraries 
import pandas as pd
import seaborn as sns 

#load data
airbnb = pd.read_csv('data/Newyork_airbnb/AB_NYC_2019.csv')

#check data
airbnb.head()
airbnb.columns

#check price columns
airbnb['price'].describe()
sns.scatterplot(x='id',y='price', data = airbnb)

#divide data frames
low_price = airbnb[airbnb.price<100]
high_price = airbnb[airbnb.price>1000]

print(airbnb.shape,low_price.shape,high_price.shape)

#concat data by rows
low_high = [low_price,high_price]
low_high_df = pd.concat(low_high)

#concat data by columns
low_high_column = pd.concat(low_high, axis = 1)
low_high_column.columns

#add hierarchical index
low_high_df_key = pd.concat(low_high , keys = ['low','high'])
low_highe_df_key.head()
low_high_df_key.tail()

#select data by extra index
#low_high_df_key.loc['low']
low_high_df_key.loc['high']

#concat based on inner join
df1 = low_price.drop('id', axis=1)
df1.columns
high_price.columns	
joined_df = pd.concat([df1,high_price], join ='inner')
joined_df
