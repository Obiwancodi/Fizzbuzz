import sys
for arg in sys.argv[0]:
  try:
    n = int(sys.argv[1])
  except IndexError:
    user_input = raw_input("Please enter a number")
    n = int(user_input)
    break
for x in range(1,n):
  if(x%3==0 and x%5==0):
    print "Fizzbuzz"
  elif(x%3==0):
    print "Fizz"
  elif(x%5==0):
    print "Buzz"
  else:
    print x