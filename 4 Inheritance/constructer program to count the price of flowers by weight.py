#WRITE A PYTHON PROGRAM TO CREATE A CLASS FLOWER WITH CLASS VARIABLE FID,FNAME
#AND COST USE CONSTRUCTER TO INITIALIZE THE VALUE AND DEF PRINT INFO THAT PRINT
#THE INFORMATION ABOUT FLOWERS AND ANOTHER DEF CHECKAMOUNT (SELF,KG)CONDITION
#FOR AMOUNT CALCULATE ARE:-
#IF KG > 5 -- 250 R/KG
#IF KG > 3 AND KG < 5 -- 180 R/KM
#ELSE -- 100 R/KM
class flower:
    fid=0
    fname=" "
    cost=0
    def __init__(self,id,name,c):
        self.fid=id
        self.fname=name
        self.cost=c
    def printinfo(self):
        print("flowers id=",self.fid)
        print("flowers name =",self.fname)
        print("flowers cost=",self.cost)
    def checkamount(self,kg):
        if kg>5:
            r=250*kg
        elif kg>3 and kg<5:
            r=180*kg
        else:
            r=100*kg
        print("Please pay =",r,"RS")
id=int(input("Ener the flowers id"))
name=input("Enter the name")
c=int(input("Enter the cost"))
obj=flower(id,name,c)
kg=int(input("Enter the number"))
obj.printinfo()
obj.checkamount(kg)





            
