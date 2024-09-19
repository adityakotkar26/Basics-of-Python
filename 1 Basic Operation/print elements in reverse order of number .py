# write a c program to print the elements of numbers in reverse order
num=int(input("Enter the number"))
sum=0
r=0
while num!=0:
    r=num%10
    print(r,end="")
    num=num//10
