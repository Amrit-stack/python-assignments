def check_u_l(str):
	u=0
	l=0
	for i in str:
		if i>='A' and i<='Z':
			u+=1
		elif i>='a' and i<='z':
			l+=1
	print('Upper case count is',u)
	print('Lower case count is',l)

a=input('Enter a string ')
check_u_l(a)