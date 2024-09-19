#write a python program to check the number is perfect or not
num=int(input("Enter the number"))
sum=0
for i in range (1,num):
    if num%i==0:
        sum=sum+i
print("",sum)
if sum==num:
    print("Number is perfect number")
else:
    print("Number is not a perfect number  ")
