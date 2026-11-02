def print_factors(x):
   print("The factors of", x, "are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = 320
print_factors(num) 

#---------------------------------------------------#

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        

