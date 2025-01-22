def access_value(dictionary, key):
    return dictionary.get(key, "Key not found")

# Example usage
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

key_to_access = 'age'
value = access_value(my_dict, key_to_access)

print(f"The value for key '{key_to_access}' is: {value}")