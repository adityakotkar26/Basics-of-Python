# write a python program to check the number is perfect square or not
num=int(input("Enter the number"))
for i in range (1,num):
    if i*i==num:
        flag=0
        break
    else:
        flag=1
if (flag==0):
    print("Perfect square number")
else:
    print("Not a perfect square number")
        
