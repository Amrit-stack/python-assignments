def change(string):
	  char = string[0]
	  string = string.replace(char, '$')
	  string = char + string[1:]
	
	  return string


a=input('Enter the string ')
print(change(a))