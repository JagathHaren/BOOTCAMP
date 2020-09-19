from Arith1 import add,sub
from Arith1.Arith2 import mul,div,mdiv
from Relate1 import greate2,small2
from Relate1.Relate2 import equal2

ch=None
while(ch!=9):
	print("\n\n----MENU----")
	print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modular Division\n6.Greater of two\n7.Smaller of two\n8.Check if equal\n9.Exit")
	num1=int(input("Enter num1:"))
	num2=int(input("Enter num2:"))
	ch=int(input("Enter your choice:"))
	if ch==1:add.add(num1,num2)
	elif ch==2:sub.sub(num1,num2)
	elif ch==3:
		obj=mul.Arith21()
		obj.mul(num1,num2)
	elif ch==4:
		obj=div.Arith22()
		obj.div(num1,num2)
	elif ch==5:
		obj=mdiv.Arith23()
		obj.mdiv(num1,num2)
	elif ch==6:greate2.greate2(num1,num2)
	elif ch==7:small2.small2(num1,num2)
	elif ch==8:
		obj=equal2.Relate21()
		obj.equal(num1,num2)
	else:
		print("----EXITING----")
		ch=9

