 dog = 'woof'

print(dog)

number = 1

while number <= 10:
  print(number)
  number += 1

def redundantFunction():
  return dog + dog

print(redundantFunction())

pythonArray = [4, 7, 2]

print(pythonArray)

arrayTotal = 0

for items in pythonArray:
  arrayTotal += items

print(arrayTotal)

def recursiveReverse(string, iteration):
  letter = string[iteration]
  if iteration == len(string) - 1:
    return letter
  else:
    return recursiveReverse(string, iteration + 1) + letter

print(recursiveReverse('woof', 0))