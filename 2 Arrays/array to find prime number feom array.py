# write a python program to print the prime numbers from array elements
import array as arr
num=arr.array("i",[])
size=int(input("Enter the size of array"))
for i in range(size):
    a=int(input("Enter the elements"))
    num.append(a)
for i in range(len(num)):
    true=0
    for j in range (2,num[i]):
        if num[i]%j==0:
            true=1
            break
        else:
            true=2
    if true==2:
        print("prime number",num[i])
