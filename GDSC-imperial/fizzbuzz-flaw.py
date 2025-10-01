# Goal: Print numbers 1 to n.
# For multiples of 3, print "Fizz".
# For multiples of 5, print "Buzz".
# For multiples of both 3 and 5, print "FizzBuzz".
# There's a logical error in this code! Can you find it?

def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 15 == 0:
            print("FizzBuzz")
        else:
            print(i)




