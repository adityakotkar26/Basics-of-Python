# write a python program to accept a array and print the even numbers of array
import array as arr
num=arr.array("i",[])
size=int(input("Enter the size"))
for i in range (size):
    a=int(input("Enter the number"))
    num.append(a)
for i in range (len(num)):
    if num[i]%2==0:
        print("",num[i])
