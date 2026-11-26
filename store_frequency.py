#Store Frequency in Dictionary
num = [5, 6, 3, 2, 1, 1, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9]

hash_map = {}
n = len(num)

for i in range(n):
    hash_map[num[i]] = hash_map.get(num[i], 0) + 1
    
print(hash_map)