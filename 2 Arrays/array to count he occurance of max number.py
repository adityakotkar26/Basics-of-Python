#write a python program to accept the array of 5 elements and print the element that occure max time
import array as arr
num=arr.array("i",[])
size=int(input("Ente the size of array"))
sum=0
count=0
max=0
for i in range (size):
    a=int(input("Enter the array element"))
    num.append(a)
max=0
for i in range (size):
    if max<=num.count(num[i]):
        max=num.count(num[i])
        element=num[i]
print("number occure max time ",element,":",max)

    
    
