# write a c program of array and print the array in reverse
import array as arr
num=arr.array("i",[])
size=int(input("Enter the size"))
for i in range (size):
    a=int(input("Enter the number"))
    num.append(a)
for i in range (len(num)-1,-1,-1):
    print(num[i])
