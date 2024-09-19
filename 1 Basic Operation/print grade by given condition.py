#write a python program to accept roll number , name , marks of 3 subject and count total average and
# grade as per the condition
a=int(input("Enter the roll number"))
b=input("Enter the name ")
c=int(input("Enter the math marks"))
d=int(input("Enter the science marks"))
e=int(input("Enter the english marks"))
total=c+d+e
print("total",total)
avg=total/3
print("avg",avg)
if avg>70 :
    print("A+ grade")
elif avg>60 and avg<70:
    printf("A grade")
elif avg>50 and avg<60:
    print("B grade ")
elif avg>40 and avg<50 :
    print("c grade")
else:
    print("fail")
      
