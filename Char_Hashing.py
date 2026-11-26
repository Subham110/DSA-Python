# Character Hashing
s = "azyxyyzaaaa"
q = {"d", "aa","a", "y", "x", "z"}

# Create a frequency dictionary for characters in s
freq_dict = {}
for char in s:
    freq_dict[char] = freq_dict.get(char, 0) + 1

# Check frequency of each character in q
for char in q:
    print(f"{char}: {freq_dict.get(char, 0)}")
