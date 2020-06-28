Bike = [{'name':'Pulsar', 'lot':100, 'color':'Black'}, {'name':'Honda', 'lot':88, 'color':'Red'}, {'name':'TVS', 'lot':97, 'color':'Blue'}]
print("Original list of dictionaries :")
print(Bike)
sorted_Bike = sorted(Bike, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_Bike)