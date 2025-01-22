string = input("Enter the string: ")

word = ''

for i in range(0, len(string)):
    if i%2 != 0:
        word += string[i]

print("Output: ")
print(word)
