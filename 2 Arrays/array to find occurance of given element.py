# write a python program of array to find  the accourance of the given element
import array as arr
num=arr.array("i",[])
size=int(input("Enter the size of array"))
n=int(input("Enter your choice"))
count=0
for i in range (size):
    a=int(input("Enter the number "))
    num.append(a)
for i in range(size):
    if num[i]==a:
        count=count+1
print("",count)
