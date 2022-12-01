from collections import Counter

# Initial Shop Inventory
my_dict = {'Apple': 0.50, 'Bannana': 0.20, 'Mango': 0.99,
		'Coconut': 2.99, 'Pineapple': 3.99}

k = Counter(my_dict)

# Finding 3 highest values
high = k.most_common(3)

print("Initial Dictionary:")
print(my_dict, "\n")


print("Dictionary with 3 highest values:")
print("Keys: Values")

for i in high:
	print(i[0]," :",i[1]," ")
