c=input("enter opertaion:")
def operation():
	a=int(input("enter a value"))
	b=int(input("enter b value"))
	if c=="add":
		d=a+b
	elif c=="sub":
		d=a-b
	elif c=="mul":
		d=a*b
	elif c=="div":
		d=a//b
	else:
		print("invalid operation")
		print("%d"(d))
operation()	
	