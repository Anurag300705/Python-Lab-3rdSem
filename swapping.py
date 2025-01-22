def swap_first_last(tup):
    if len(tup) < 2:
        return tup
    return (tup[-1],) + tup[1:-1] + (tup[0],)

# Example usage
my_tuple = (10, 20, 30, 40)
swapped_tuple = swap_first_last(my_tuple)
print("Tuple after swapping:", swapped_tuple)