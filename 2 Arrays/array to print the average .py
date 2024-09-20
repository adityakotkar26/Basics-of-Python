#write a python program of array to print the average
import array as arr
num=arr.array("i",[])
size=int(input("Enter the size of array"))
sum=0
avg=0
for i in range(size):
    a=int(input("Enter the number"))
    num.append(a)
for i in range (len(num)):
    sum=sum+num[i]
    avg=sum/size
print("Average of given numbers=",avg)
