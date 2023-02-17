def fibonacci(num):
  a, b = 0, 1
  while(a < num):
    yield a
    a, b = b, a + b
    
x = fibonacci(5)  # iterator object
for x in x:
  print(x)
