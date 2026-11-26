n = 5632

num = n
while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10
    
#---------------------------------------------------#
#count a number of digits in a number
n = 563211
num = n
count = 0
while num > 0:
    count += 1
    num = num // 10
print("Number of digits:", count)