# wapp to print the sum of numbers from string
str1=input("Enter the string")
for i range (len(str1)):
    if str1[i]>="0" and str1[i]<="9":
        sum=sum+str1[i]
    print(sum)
