# write a python program to accept a array and find the second heighest element
# of array
import array as arr
ans=arr.array("i",[])
for i in range (5):
    for j in range (i+1,5,):
        if ans[i] > ans[j]:
            ans[j],ans[i]=ans[i],ans[j]
print(ans[1])
