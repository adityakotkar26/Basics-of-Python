# WRITE A PYTHON PRORAM WITH CLASS TRIAL WITH CLASS VARIABLE A AND B USE CONSTRUCTOR TO INITILIZE THE
# VALUE AND DEFINATION GETINFO(SELF) CREATE ANOTHER CLASS DEMO THAT EXTENDS ABOVE CLASS , WITH CLASS
# VERIABLE C AND DEFINATION PRINT DETAIL.
class Trial:
    a=0
    b=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def getinfo(self):
        print("a=",a,"b=",b)
class demo (Trial):
    c=0
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def getinfo1(self):
        print("c=",c)
a=int(input("Enter a="))
b=int(input("Enter b="))
c=int(input("Enter c="))
obj=demo(a,b,c)
obj.getinfo()
obj.getinfo1()
