#write a python program to check the number is perfect or not
n=int(input("Enter the number "))
sum=0
i=1
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if sum==n:
    print("it is a perfect number")
else:
    print("it is not a perfect number ")
