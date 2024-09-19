#write a python program to print the sum of even and odd numbers seperetly
n=int(input("Enter the number"))
osum=0
esum=0
i=0
while i<=n:
    if(i%2==0):
        esum+=i
    else:
        osum+=i
    i=i+1
print("Even=",esum)
print("odd=",osum)
    
