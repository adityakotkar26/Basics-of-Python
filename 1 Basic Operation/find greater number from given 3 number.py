#write a python program to accept 3 number and find the max number from 3 numbers
a=int(input("Enter the first number "))
b=int(input("Enter the second  number "))
c=int(input("Enter the third number "))
if (a>b and a>c):
    print("",a,"is the maximum number ")
elif (b>a and b>c ):
    print("",b,"is the maximum number ")
else:
    print("",c,"is the maximum number ")
