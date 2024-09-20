# write a python program of array to checkthe dublicateelements of array and remove it
import array as arr
num=arr.array("i",[])
size=int(input("Enter the size of elements"))
for i in range(size):
    a=int(input("Enter the elements"))
    num.append(a)
for i in range (len(num)):
    for j in range (i+1,len(num)):
        if num[i]==num[j]:
            num[j]=0
for i in range (len(num)):
    if num[i]!=0:
        print("",num[i])
