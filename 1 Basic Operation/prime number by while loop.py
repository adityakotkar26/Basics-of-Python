#write a python program to check number is prime or not
n=int(input("Enter the number "))
i=2
while i<n:
    if n%i==0:
        flag=0
        break
    else :
        flag=1
    i=i+1
if(flag==0):
    print("Number is not prime")
else:
    print("Number is prime")
