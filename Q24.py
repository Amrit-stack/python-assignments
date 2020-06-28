def copy(mylist):
	copied_list=mylist[:]
	return mylist

mylist=[1,2,3,4,5]
print('Original list: ',mylist)
print('copied list: ',copy(mylist))
