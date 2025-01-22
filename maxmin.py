def find_max_min(lst):
    # Find the maximum element using the max() function
    max_element = max(lst)
    # Find the minimum element using the min() function
    min_element = min(lst)
    
    return max_element, min_element

# Example usage:
my_list = [23, 1, 45, 78, 3, 99, 12]

max_value, min_value = find_max_min(my_list)
print(f"The maximum element in the list is: {max_value}")
print(f"The minimum element in the list is: {min_value}")