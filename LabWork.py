#immutable and mutable

# List is mutable 

f = [1,2,3, "Anurag"]
print(f)

f.insert(2,45) # Inserts 45 at index 2
print(f)

f[2] = "Python" # Inserts Python at index 2
print(f)

f.append(35) # adds element 35 to end of list
print(f)
print(type(f))

f1 = (1) # If tuple has 1 element, it is converted to its respective data type
print(type(f1))

# String is also a type of list but it is immutable

s = "Anurag"
# s[2] = "O" This is not possible as string cannot be changed
print(s[2])

a = ("Anurag", 1, 2, "Yes")
print(a)
print(type(a))
a1 = list(a) # Converts tuple to list
print(type(a1)) 

d = {"Anurag", 1, 2, 2} # Set does not print duplicate elements
# d[1] = 5
print(d)
print(type(d))

d1 = {"A" : 35, "B" : 45}
d1["A"] = 56 # Dictionary can also change value according to keys
print(d1)
print(type(d1))

# d2 = {}
# k1 = int(input("Enter number"))
# k2 = int(input("Enter number"))

# d2({k1,k2})  Not possible as dictionary is not callable
# print(d2)

# d2 = {}
# k1 = input("Enter word")
# k2 = int(input("Enter number"))
# d2({k1:k2})  Dictionary is not callable
# print(d2)

user_dict = {}
num_entries = int(input("Enter the number of entries you want to add: "))
for i in range(num_entries):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value
print("Dictionary after adding user input:", user_dict)

d2 = {}
k1 = input("Enter word: ")
k2 = int(input("Enter number"))
d2.update({k1:k2})  
print(d2)

def fun1(x):
    print("This is function1 and the value is: ", x)

fun1(4)

