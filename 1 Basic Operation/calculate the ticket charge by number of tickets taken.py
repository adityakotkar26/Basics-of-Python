#write a python program to enter the viewer id,name,number of tickets,and gender calculate ticket cost
# and if viver if femal then give 20% more disscount
id=int(input("Enter the viewer id "))
n=input("Enter the viewer name : ")
no_t=int(input("Enter the number of tickets:"))
g=input("Enter the gender of viewer (m/f):")
if no_t>15:
    c=no_t*300
    print("Please pay:",c)
elif no_t>12 and no_t<15:
    c=no_t*200
    print("Please pay:",c)
else:
    c=no_t*100
    print("please pay :",c)
if g=="f":
    d=c*(20/100)
    c-=d
    print("Please pay : ",c)
