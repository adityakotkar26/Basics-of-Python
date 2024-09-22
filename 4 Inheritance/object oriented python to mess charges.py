# WRITE A PYTHON PROGRAM WITH CLASS MESS WITH DEF GET_INFO (SELF,DISHTYPE,NO_OF_
#DAYS )
#IF DISHTYPE="VEG" - 100R/D
#IF DISHTYPE="NON-VEG"- 250 R/D
class mess:
    def getinfo(self,id,name,city):
        print("id=",id,"name=",name,"city",city)
    def charges(self,disht,d):
        if disht=="veg":
            r=100*d
        else:
            r=250*d
        print("Please pay =",r,"rs")
obj=mess()
id=int(input("Enter the id"))
name=input("Enter the name ")
city=input("Enter the city")
disht=input("Select veg or non veg")
d=int(input("Enter the number of dishes"))

obj.getinfo(id,name,city)
obj.charges(disht,d)
