# write a python program to print the elements in accending order
import array as arr
ans=arr.array("i",[85,9,8188,17,855,-9,81,-35,0,-885])
for i in range (len(ans)):
    for j in range (i+1,len(ans)):
        if ans [i]>ans[j]:
            ans[j],ans[i]=ans[i],ans[j]
for i in range (len(ans)):
    print(ans[7],ans[8],ans[9])
