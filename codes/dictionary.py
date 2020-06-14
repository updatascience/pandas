#Create dictionary
dataDictionary = {
    'price':1000,
    'room_type':'Apartment',
    'build_year':1960,
    'location':'Center',
    'xxxx':'yyyyy'
}

#find type 
type(dataDictionary)

#retrieve values
dataDictionary['location']
dataDictionary['location2']
print(dataDictionary.get('location2'))

#retrieve keys
for key in dataDictionary:
    print(key)
	
#retrieve values
for key in dataDictionary:
    print(dataDictionary[key])
	
#find out length
print(len(dataDictionary))

#delete value
dataDictionary.pop('location')
dataDictionary

#update value
dataDictionary['price'] = 2000

#remove whole object
dataDictionary.clear()