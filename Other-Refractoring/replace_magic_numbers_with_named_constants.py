# by Kami Bigdely 
# Replace magic numbers with named constanst

# First Section
# Given two point charges, calcualte the electric force exerted on them.
COULUMB_CONSTANT = 8.9875517923*1e9
q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance be10tween two charges: "))
force = COULUMB_CONSTANT * q1 * q2/(distance**2)
print ("Electric Force between q1 and q2 is: ", force, "Newton")

# Second Section
MODULUS_EVEN = 2
num = int(input('Enter an integer number: '))
if num % MODULUS_EVEN == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")