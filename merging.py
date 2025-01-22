def merge_sorted_lists(list1, list2):
    # Initialize pointers for list1 and list2
    i, j = 0, 0
    merged_list = []
    
    # Traverse both lists and append the smaller element to merged_list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # If there are remaining elements in list1, add them to merged_list
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # If there are remaining elements in list2, add them to merged_list
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1