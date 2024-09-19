#write a python program to find the min number from 3 numbers
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
if (a<b and a<c):
    print("",a,"Is the minimum number")
elif (b<a and b<c):
    print("",b,"Is the minimum number")
else :
    print("",c,"Is a minimum number")
