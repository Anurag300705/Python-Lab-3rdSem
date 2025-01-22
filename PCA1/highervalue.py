def super_name(name1, name2):

    if len(name1)==len(name2):
        sum1 = sum(ord(char) for char in name1)
        sum2 = sum(ord(char) for char in name2)
    
        if sum1 > sum2:
            return name1
        elif sum2 > sum1:
            return name2
        else:
            return "Both names have equal ASCII value sums"
    else:
        return "Names should have same length"    

# Test cases
print("The name with higher ascii value is: ")
print(super_name("Deep", "Raju"))  
print(super_name("Anurag", "Ankan"))    
