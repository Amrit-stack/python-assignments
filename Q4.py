def mix(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b


a=input('1st string ')
b=input('2nd string ')
print(mix(a,b))
