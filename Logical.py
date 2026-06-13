#Write a Python program to show how the logical not operator is used to reverse conditions and check whether values are different.
# Program to check the application of logical not operator

a = 10
b = 12
c = 12

# not is used here to reverse the result of (a == b)
print(not (a == b))

# not is used here to reverse the result of (b == c)
print(not (b == c))
    print(a, 'and', b, 'are different')

a = 4
b = 5

# not is used here to reverse the result of comparing both conditions
if not ((a == 1 ) == (b == 5)):
    print('Hello')

a = int(input("Enter a number: "))

# not is used here to check that the number is not even
if not (a % 2 == 0):
    print(a, "is an odd number")

    