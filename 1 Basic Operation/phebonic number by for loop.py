#write a c program to print the phebonic series
n=int(input("Enter the number"))
first=1
last=1
next=1
i=3
print(first,end=" ")
print(last,end=" ")
for i in range (3,n+1):
    next=first+last
    print(next,end=" ")
    first=last
    last=next
