def add_string(string):
	if len(string)>=3:
	    if string[-3:]!='ing':
	    	return string+'ing'
	    else:
	    	return string[:-3]+'ly'
	else:
		return string
	
a=input('Enter the string ')
print(add_string(a))