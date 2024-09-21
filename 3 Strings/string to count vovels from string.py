# WRITE A PYTHON PROGRAM TO COUNT THE VOVELS FROM THE STRING
str=input("Enter the string ")
count=0
for i in range (len(str)):
    if str[i]=='a' or  str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u' :
        count =count+1
print("count=",count)
