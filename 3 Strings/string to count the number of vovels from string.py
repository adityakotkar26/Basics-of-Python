# write a python program to accept a string and count the vowels from given string.
str=input("Enter the string")
count=0
for i in range(len(str)):
    if str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u":
        count=count+1
        print("vovels are",str[i])
print("number of vovels :",count)
