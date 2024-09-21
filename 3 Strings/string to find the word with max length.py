# WRITE A PYTHON PROGRAM TO PRINT THE WORD WITH MAX LENGTH
str=input("Enter the string")
ans=str.split(" ")
max=ans[0]
for i in range (len(ans)):
    if len(ans[i])>len(max):
           max=ans[i]
print("max word-",max)
