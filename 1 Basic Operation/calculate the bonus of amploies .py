# write a cpython pogram to accept amploie age and salary and print the bonus by the condition given
age=int(input("Enter the Emploie age"))
s=int(input("Enter the Emploie salary"))
if age>60:
    b=s*5/100
elif age>35 and 60>age:
    b=s*10/100
else:
    b=s*15/100
print("Bonous amount is : ",b)

