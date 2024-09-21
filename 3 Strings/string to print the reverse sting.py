#print the gives  string in reverse order
str1=input("Enter the string")
temp=0
for i in range(len(str1)):
    for j in range(1,len(str1)):
        if str1[i]>str1[j]:
            temp=str1[i]
            str1[i]=str1[j]
            str1[j]=temp
print(str1)
