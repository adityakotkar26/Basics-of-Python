# write a python program to print the sum of even and odd elements from number
num=int(input("Enter the number"))
esum=0
r=0
osum=0
while num!=0:
    r=num%10
    if r%2==0:
        esum+=r
    else:
        osum+=r
    num=num//10
print("sum of even digits",esum)
print("sum of odd numbers ",osum)
