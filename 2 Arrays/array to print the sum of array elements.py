#write a python program to print the sum  of array elements
import array as arr
num=arr.array("i",[])
sum=0
size=int(input("Enter the size of array"))
for i in range(size):
    a=int(input("Enter the number"))
    num.append(a)
for i in range (len(num)):
    sum=sum+num[i]
print("sum of all array elements=",sum)
