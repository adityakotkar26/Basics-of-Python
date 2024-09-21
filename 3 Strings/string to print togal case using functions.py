# write a pythton p to accept a sring and print the string in togalcase
str1=input("Enter the string")
ans=""
for i in range(len(str1)):
    if i%2==0:
        ans=str1[i].upper()
    else:
        ans=str1[i].lower()
    print(ans,end="")
        
