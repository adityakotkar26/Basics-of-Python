# WRITE A PYTHON PROGRAM TO COUNT THE UPPER CASE LOWER CASE DIGITS AND SYMBOLS
str=input("Enter the string ")
up=0
lw=0
di=0
sy=0
for i in range (len(str)):
    if str[i]>='A' and str[i]<='Z':
        up=up+1
    elif str[i]>='a' and str[i]<='z':
        lw=lw+1
    elif str[i]>='0' and str[i]<='9':
        di=di+1
    else:
        sy=sy+1
print("upper case elements = ",up)
print("lower case elements = ",lw)
print("digits = ",di)
print("symbols = ",sy)
