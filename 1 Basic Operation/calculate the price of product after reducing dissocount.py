#write a python program to accept a product id,name,cost,and payment type .calculate disscount with
# following condition . if type is by cash provide 3% extra disscount
id= int(input("Enter the product id :"))
n=input("Enter the product name :")
c=int(input("Enter the product cost:"))
t=input("Enter the payment type :")
if c>300:
    d=c*10/100
    p=c-d
elif c>200 and c<300:
    d=c*8/100
    p=c-d
else:
    d=c*5/100
    p=c-d
if t=="cash":
    x=c*3/100
    p-=x
print("please pay :",p)
