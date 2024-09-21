#  WRITE A PYTHON PROGRAM TO CALCULATE THE @ SYMBOLS AND IF IT IS 1 THEN PRINT
# VALID EMAIL
str=input("Enter the string ")
count=0
for i in range (len(str)):
    if str[i]=='@':
        count=count+1
if count!=1:
    print("invalid email")
else:
    print("Valid email")
