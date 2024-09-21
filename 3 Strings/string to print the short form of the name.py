#enter the name and print hte short form of the name
str1=input("Enter the first name")
ans=""
temp=str1.split(" ")
ans=temp[0]
print(ans[0].upper(),".",end=' ')
ans1=temp[1]
print(ans1[0].upper(),".",end=' ')
print(temp[len(temp)-1].upper())
