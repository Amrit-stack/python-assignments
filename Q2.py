def show_bothends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

a=input('Enter the string\t')
print(show_bothends(a))

