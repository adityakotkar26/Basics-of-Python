# write a p p and count the ocurance of the waord
str=input("Enter the string")
count=0
for i in range(len(str)):
    if str[i]==" " and str[i+1]=="t" and str[i+2]=="h" and str[i+3]=="e":
        count=count+1
print("count :",count)
