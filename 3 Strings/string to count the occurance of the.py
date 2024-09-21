str1=input("Enter the string")
count=0
for i in range(len(str1)):
    if str1[i]==" " and str1[i+1]=="t" and str1[i+2]=="h" and str1[i+3]=="e" and str1[i+4]==" ":
        count=count+1
print(count)
