#write a python program to count upper case  loweer  digit and spesial symbols
str=input("Enter the string")
up=0
lw=0
di=0
sy=0
for i in range(len(str)):
    if str[i]>="A" and str[i]<="Z":
        up=up+1
    elif str[i]>="a" and str[i]<="z":
        lw=lw+1
    elif str[i]>="0" and str[i]<="9":
        di=di+1
    else:
        sy=sy+1
print("Number of upper case elements:",up)
print("Number of lower case elements:",lw)
print("Number of digits:",up)
print("Number of symbols:",sy)
