def count_occurrences(tup, element):
    return tup.count(element)
# Example usage
my_tuple = (1, 2, 3, 4, 2, 5, 2, 6)
element_to_count = 2
occurrences = count_occurrences(my_tuple, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the tuple.")