#Prestor values into same datastructer like List/Dictionary/Set and then feting the values from it. This is called Hashing.

n = [5,3,2,2,1,5,5,7,5,10,10]
m = [10,111,1,9,5,67,2]

#First Method
"""
for i in m:
    count = 0
    for x in n:
        if x == i:
            count += 1
    print(f"{i}: {count}") #it show the TLE ( Time Limit Exicted)
"""   

#Second Method
hash_list = [0]*11
for i in n:
    hash_list[i] += 1

for i in m:
    if i < 1 or i >10:
        print(f"{i}: 0")
    else:
        print(f"{i}: {hash_list[i]}")


#Third Method       
'''
In DIctionary we can store the values in key value pair and then we can fetch the values from it. It is called Hashing. """   
print("----------------------------------------------------#") 
frq_dict = {}
for i in n:
    frq_dict[i] = frq_dict.get(i, 0) + 1    

for i in m:
    print(f"{i}: {frq_dict.get(i, 0)}")

'''