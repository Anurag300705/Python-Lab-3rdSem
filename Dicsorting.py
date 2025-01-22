my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

# Sort the dictionary by values
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Output the sorted dictionary
print(sorted_dict)