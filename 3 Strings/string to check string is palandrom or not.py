# write a python program to check string is palandrom or not
str=input("Enter the string")
ptr=(str[::-1])
if str==ptr:
    print("String is palandrom ")
else:
    print("String is non palanrom ")
