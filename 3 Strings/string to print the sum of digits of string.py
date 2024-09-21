# wapp to print the sum of numbers from string
str1=input("Enter the string")
aa = len(str1)
sum=0
for i in range(aa):
    if str1[i]>='0' and str1[i] <='9':
        sum=sum+int(str1[i])
print("Sum of digit",sum)
