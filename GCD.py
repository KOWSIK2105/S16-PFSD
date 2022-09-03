# importing math module
import math
# function which computes and returns the highest common factor of the given two numbers
def findGcd(number1, number2):
    # calculating gcd using gcd() function
    resGcd = math.gcd(number1, number2)
    # return the gcd of the number 1 and number2
    return resGcd
# given two numbers
# given number a
number1 = 24
# given number b
number2 = 36
# passing the given two numbers to findGcd function which returns the greatest common factor of the given two numbers
ans = findGcd(number1, number2)
# print the hcf of the given two numbers
print("The Highest Common Factor (HCF) of the numbers", number1, number2, "=", ans)
