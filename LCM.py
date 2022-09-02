# importing math
import math
# given two numbers
# given number a
number1 = int(input())
# given number b
number2 = int(input())
# finding lcm of the given two values
lcmValue = (number1*number2)//math.gcd(number1, number2)
print("The LCM of the given two numbers",
      number1, ",", number2, "=", lcmValue)