
def find_lowest_distance(num1, num2):
    
    str_num1 = str(num1)
    str_num2 = str(num2)

    min_length = min(len(str_num1), len(str_num2))

    min_distance = float('inf')
    digit1 = None
    digit2 = None

    for i in range(min_length):
        d1 = int(str_num1[i])
        d2 = int(str_num2[i])

        distance = abs(d1 - d2)

        if distance < min_distance:
            min_distance = distance
            digit1 = d1
            digit2 = d2

    # Check if a valid distance was found
    if digit1 is not None and digit2 is not None:
        print("Distance:", min_distance,", Digits are", digit1 ,"and", digit2)
    else:
        print("Distance not found")

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
find_lowest_distance(num1, num2)