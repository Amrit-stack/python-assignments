mylist=[1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list=[]
for num in mylist:
	if num%2==0:
		even_list.append(num)
	else:
		continue

print(even_list)