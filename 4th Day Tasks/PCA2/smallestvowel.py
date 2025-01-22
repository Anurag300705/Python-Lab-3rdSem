string = input("Enter a string: ")

vowels = "aeiou"

is_vowel = []

for char in string.lower():
    if char in vowels:
        is_vowel.append(char)

print(f"The smallest vowel is: {min(is_vowel)}")

