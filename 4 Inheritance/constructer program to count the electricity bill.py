#WRITE A PYTHON PROGRAM WITH CLASS ELECTRICITY BILL WITH CLASS VAR,METER ID ,
#USER NAME ADDRESS USE CONSTRUCTER TO INITIALIZE THEVALUE AND DEF PRINT INFO
#AND CLASS ALSO HAVING ANOTHER DEF INFOCHARGES (SELF,UNIT)
#IF UNIT > 300 -- 5RS/UNIT
#IF UNIT > 100 AND < 300 -- 8RS/UNIT
#ELSE -- 12 RS/KM
#ALSO AND 5% AS DEPOSITE CHARGES 3% AS A INSPECTION CHARGES AND 8% AS A METER CHARGES
class electricitybill:
    meterid=0
    username=" "
    address=" "
    def __init__(self,id,name,add):
        self.meterid=id
        self.username=name
        self.address=add
    def printinfo (self):
        print("Meter id =",self.meterid)
        print("username=",self.username)
        print("address=",self.address)
    def getinfocharges (selg,unit):
        if unit>300:
            r=5*unit
        elif unit>100 and unit<300:
            r=8*unit
        else:
            r=12*unit
        d=(5/100)*r
        i=(3/100)*r
        m=(8/100)*r
        total=r+d+i+m
        print("Please Pay = ",total)
id=int(input("Enter the id="))
name=input("Enter your name=")
add=input("Enter your aderss=")
obj=electricitybill(id,name,add)
obj.printinfo()
unit=int(input("Enter the unit"))
obj.getinfocharges(unit)














            
