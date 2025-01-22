def factorial(n):
    fact = 1
    for i in range(1,(n+1)):
        fact*=i
    return fact

a = int(input("Enter the number: "))
o = a
sum = 0
s = 0
while(a!=0):
    s = a%10
    sum += factorial(s)
    a //= 10
if sum == o:
    print(o ,"is a Strong number")
else:
    print(o ,"is not a Strong number")        
