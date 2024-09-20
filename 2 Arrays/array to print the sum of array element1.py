# write a python program to accet the array and and print the sum of array element
import array as arr
num=arr.array("i",[])
size=int(input("Ente the size of array"))
sum=0
for i in range(size):
    a=int(input("Enter the element"))
    num.append(a)
for i in range(size):
    sum=sum+num[i]
print("sum of elements :",sum)
