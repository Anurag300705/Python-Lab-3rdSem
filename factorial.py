n = int(input("Enter the number: "))
fact = 1
if n==1 or n==0:
    print("1")
else:    
    for i in range(1,n+1):
        fact *= i
    print("The factorial of",n,"is",fact)    