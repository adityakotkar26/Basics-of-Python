#write a python program student with def getdetail(self,id,name,stream )create
#another class exam that extends above class with def calculate grade (self,a,b,c)
# the defination calculate total avg and grade
class student:
    def getdetail(self,id,name,stream):
        print("Id=",id,"name=",name,"stream=",stream)
class exam(student):
    def calgrade(self,a,b,c):
        avg=(a+b+c)/3
        print("avg=",avg)
        if avg>=75:
            print("A+ Grade")
        elif avg>=60 and avg<75:
            print("A Grade")
        elif avg>=50 and avg<60:
            print("B Grade")
        elif avg>=40 and avg<50:
            print("C Grade")
        else:
            print("fail")
obj=exam()
id=int(input("Enter the id"))
name=input("Enter the name")
stream=input("Enter the stream")
a=int(input("Enter the maths marks"))
b=int(input("Enter the science marks"))
c=int(input("Enter the english marks "))
obj.getdetail(id,name,stream)
obj.calgrade(a,b,c)
