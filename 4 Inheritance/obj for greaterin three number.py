def greater(x,y,z):
    if x>=y and x>=z:
        print(x,"is a greatest number")
    elif y>=x and y>=z:
        print(y,"is a greatest number")
    else:
        print(z,"is a greatest number")
x=int(input("Enter the first number :"))
y=int(input("Enter the second number :"))
z=int(input("Enter the third number :"))
greater(x,y,z)
