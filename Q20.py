def q20(string):
  counter = 0

  for i in string:
    if len(i) > 1 and i[0] == i[-1]:
      counter += 1
  return counter

print(q20(['abc', 'xyz', 'aba', '1221']))