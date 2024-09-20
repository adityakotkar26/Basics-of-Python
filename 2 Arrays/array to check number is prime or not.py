# write a python profgram to acceptt the array of 10 elements and print the prime number
# from those array elements
import array as arr
num=arr.array("i",[])
for i in range(10):
    a=int(input("Enter the element"))
    num.append(a)
for i in range(10):
    if num%i==0:
        true=1
        break
    else:
        true=2
if true==2:
    print("prime number",num[i])
    
