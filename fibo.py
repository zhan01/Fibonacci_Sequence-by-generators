print("\n-----Fibonacci Sequence-----\n")
def fib(num):
  a,b = 0, 1
  for i in range(0, num):
    yield "{}:: {}".format(i + 1,b)
    a, b = b, a + b

for item in fib(7):
  print (item)

