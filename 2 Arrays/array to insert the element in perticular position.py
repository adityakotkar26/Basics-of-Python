# write a python program to accept the array of 10 elements and incert the element
# at perticular position as per value.
import array as arr
ans=arr.array("i",[])
for i in range(10):
    num=int(input("Enter the number"))
    ans.append(num)
value = int(input("Enter the number to insert"))
ans.append(value)
for i in range (len(ans)):
    for j in range (i+1,len(ans)):
        if ans [i]>ans[j]:
            temp = ans[i]
            ans[i]=ans[j]
            ans[j] = temp
for i in range (len(ans)):
    print(ans[i])

