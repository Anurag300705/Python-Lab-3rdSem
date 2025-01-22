def is_subset(set1, set2):
    return set1.issubset(set2)

# Example usage
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if is_subset(set1, set2):
    print(f"{set1} is a subset of {set2}")
else:
    print(f"{set1} is not a subset of {set2}")