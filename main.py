# program to find if a number is Armstrong NUmber


# Take input from the user
number = int(input("Enter a number: "))

# Calculate number of digit
degits = len(str(number))

# Initialize result variable
resultNumber = 0

# find the sum of the a^digits of each digit
temp = number
while temp> 0:
    digit = temp % 10
    resultNumber += digit**degits
    temp //= 10

# display the result
if number == resultNumber:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")