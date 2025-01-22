def string_count(list):
    valid = 0
    invalid = 0

    for s in list:
        if all(char.isalpha() or char.isspace() for char in s):
            valid += 1
        else:
            invalid += 1

    return valid, invalid

def check_validity(str):
    for char in str:
        if all(char.isalpha() or char.isspace() for char in str):
            return 'valid'
        else:
            return 'invalid'


str = input("Enter a string : ")
print("The character is: ", check_validity(str))

list = [ "Hello World", "Surplus", "123Iam", "Another String again", "Valid?!@#", "345", "Anurag" ]

valid, invalid = string_count(list)
print(f"Valid strings: {valid}") 
print(f"Invalid strings: {invalid}")
