# write a python program to check the number is amstrong or not
num=int(input("Enter the number "))
sum=0
r=0
temp=num
while num!=0:
    r=num%10
    sum=sum+(r*r*r)
    num=num//10
if temp==sum:
    print("Number is amstrong ")
else:
    print("Number is not amstrong")
