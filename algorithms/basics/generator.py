def upto(n):
  for i in range(n+1):
    # The yield statement is what makes a function 
    # a generator
    yield i
for number in upto(5):
  print(number)