def set_op(set1, set2):
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    difference = set1.difference(set2)
    
    return union, intersection, difference

# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union, intersection, difference = set_op(set1, set2)

print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference (set1 - set2): {difference}")