n = int(input("Enter the range upto n terms: \n"))
a = 0
b = 0
c = 1
print("The fibonacci numbers are: ")
for i in range(1,n+1):
    a = a+b
    b=c
    c=a
    print(a)