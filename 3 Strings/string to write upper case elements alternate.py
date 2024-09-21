# WRITE A C PROGRAM TO PRINT THE GIVEN STRING IN CAPITAL IF EVEN POSITION
str=input("Enter the string")
ans=str.upper()
ans1=str.lower()
for i in range (len(str)):
    if i%2==0:
        print(" ",ans[i],end=" ")
    else :
        print(" ",ans1[i],end=" ")
