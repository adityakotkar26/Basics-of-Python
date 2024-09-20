# write a python program to accept 10 elements and print max 3 elements
import array as arr
ans=arr.array("i",[])
size=int(input("Enter the size"))
for i in range(size):
    a=int(input("Enter the number "))
    ans.append(a)
for i in range (len(ans)):
    for j in range (i+1,len(ans)):
        if ans [i]<ans[j]:
            ans[j],ans[i]=ans[i],ans[j]
print(ans[0],ans[1],ans[2])

        

            
