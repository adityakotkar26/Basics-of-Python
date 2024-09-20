# WRITE A PYTHON PROGRAM TO ACCEPT 10 ARRAY ELEMENTS AND PRINT MAXIMUM SEQUENCE SERIES OF ARRAY
import array as arr
ans=arr.array("i",[])
size=int(input("Enter the size"))
for i in range(size):
    a=int(input("Enter the number "))
    ans.append(a)
for i in range (len(ans)):
    for j in range (i+1,len(ans)):
        if ans [i]>ans[j]:
            ans[j],ans[i]=ans[i],ans[j]
for i in range (len(ans)):
    print(ans[i])

    
