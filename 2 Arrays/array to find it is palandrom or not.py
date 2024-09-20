# write a python program of array to check the array is palandrom or not
import array as arr
num=arr.array("i",[])
size=int(input("Enter the size of array"))
for i in range (size):
    a=int(input("Enter the elements"))
    num.append(a)
for j in range (len(num)):
    if num[i]==num[j]:
        flag=1
        break
    else:
        flag=0
        break
   
if flag==1:
    print("Array is palandrom")
else:
    print("Array is non palandrom")
