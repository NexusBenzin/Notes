# Functions are used to simplify the code when doing the same thing multiple times
# For example counting the sum of something

# We can define a Function

def sum(a,b):
    print(a+b)

# Now if we have to numbers that we need the sum of, we can use our new functions "sum()"

number1 = 1
number2 = 2

sum(number1,number2)

# We can also make it so that instead of printing the sum, our function "returns" the sum

def sum2(a,b):
    return a+b

result = sum2(number1,number2)
print(result)