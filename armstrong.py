x=0
n=0
a=int(input("Enter the number: "))
b=a
c=b
while(a>0):
	n+=1
	a=a//10
while(b>0):
	x=x+pow((b%10),n)
	b=b//10
if x==c:
	print("The no. is armstrong")
else:
	print("The no. is not armstrong");