#write a python program to accept the array of 10 elements and join the array
# having commom values .
import array as arr
num=arr.array("i",[])
for i in range(10):
    a=int(input("Entre the element"))
    num.append(a)
for i in  range(10):
    for j in range(i+1,10):
        if num[i]==num[j]:
            ans=num[i]
        print(ans)
