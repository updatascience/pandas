import pandas as pd #load pandas
airbnb = pd.read_csv('data/Newyork_airbnb/AB_NYC_2019.csv') #read dataset

airbnb.head() #check head of dataset
airbnb['neighbourhood_group']=='Manhattan' # filter neighbourhood group

airbnb[airbnb['neighbourhood_group']=='Manhattan'] #apply condition
airbnb[airbnb['price']>300] # filter rows based on price value
airbnb[airbnb['neighbourhood_group'].isin(['Manhattan'])] # filter rows based on isin function
#combine conditions
airbnb[(airbnb['neighbourhood_group']=='Manhattan') & (airbnb['price']>300)]
airbnb[airbnb['neighbourhood_group'].isin(['Manhattan','Brooklyn'])]
airbnb.filter(['neighbourhood_group','price','room_type'])
#use filter function
airbnb.filter(regex='review')
airbnb.filter(like='review')
airbnb.filter(like='1', axis=0)                                                           