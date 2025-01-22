def area():
    print("This is simple area")

def area(a):
    print(f"This is new area a = {a}")

def area(a,b):
    print(f"This is new area a = {a} and b = {b}")

# area()  Uncommenting this line shows an error as two arguments must be passed
# area(5) Uncommenting this line shows an error as two arguments must be passed and only one parameter must be passed
area(5,6)