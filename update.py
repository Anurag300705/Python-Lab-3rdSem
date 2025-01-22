def add_or_update(dictionary, key, value):
    dictionary[key] = value
    return dictionary

# Example usage
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Adding a new key-value pair
my_dict = add_or_update(my_dict, 'profession', 'Engineer')

# Updating an existing key-value pair
my_dict = add_or_update(my_dict, 'age', 26)

print(my_dict)