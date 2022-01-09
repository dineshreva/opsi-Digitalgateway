print("Please Enter the value ")
x=input("Enter first number ")
y=input("Enter second number ")
def sum(x,y):
	print("Sum of two number ",(int(x)+int(y)))
def sub(x,y):
	print("Sum of two number ",(int(x)-int(y)))
def mult(x,y):
	print("Sum of two number ",(int(x)*int(y)))

if __name__ == "__main__":
	z=input("Enter operation : ")
	if "sum"==z:
		sum(x,y)
	elif "sub"==z:
		sub(x,y)
	elif "mult"==z:
		mult(x,y)
	else:
		print("No Operation has specified  ")
		print("Hello")

	
