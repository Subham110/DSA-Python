n = int(input("Enter the number to check if it is an Armstrong number: "))

num = n
total = 0
num_digits = len(str(n))

while num > 0:
    last_digit = num % 10
    total = total + last_digit ** num_digits
    num = num // 10
    
print("The original number is:", n)
print("The sum of the digits raised to the power of the number of digits is:", total)

if n == total:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")