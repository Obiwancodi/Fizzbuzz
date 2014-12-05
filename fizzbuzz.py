import sys

#$ python fizzbuzz.py
#sys.argv = ??
#['fizzbuzz.py']

#$ python fizzbuzz.py 15 20 animal
#sys.argv = ??
#['fizzbuzz.py', '15', '20', 'animal']

# python fizzbuzz.py            => ask for a number 
# python fizzbuzz.py 10         => fizzbuzz with 10
# python fizzbuzz.py ten        => error integer only => ask for a number
# python fizzbuzz.py 10 30 junk => error integer only => ask for a number

# zero-indexed

print sys.argv
flag = True
if len(sys.argv) > 1:
    user_input = sys.argv[1]
else:
    user_input = "wrong"
while flag:
    try:
        n = int(user_input)
        # if it all works, great
        flag = False
    except ValueError:
        user_input = raw_input("Please enter a integer: ")
    
for x in range(1, n+1):
  if x % 3 == 0 and x % 5 == 0:
    print "Fizzbuzz"
  elif x % 3 == 0:
    print "Fizz"
  elif x % 5 == 0:
    print "Buzz"
  else:
    print x