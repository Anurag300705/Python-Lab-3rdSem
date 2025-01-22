string = input("Enter a string: ")

v = 0   # To count vowels 
c = 0   # To count consonants

vowels = "aeiouAEIOU"

for char in string:
    if char.isalpha():
        if char in vowels:
            v += 1
        else:
            c += 1

print("Number of vowels:", v)
print("Number of consonants:", c)
