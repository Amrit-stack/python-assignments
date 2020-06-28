from functools import reduce
  
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1]) 

a=int(input('How many terms? '))  
print(fib(a)) 