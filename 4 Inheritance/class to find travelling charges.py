#WRITE A P P  WITH CLASS TRAVELLER HAVING A DEF SHOWDETAIL(SELF,ID,NAME,CITY) CREATE ANOTHER DEFINATION
#CALCULATE CHARGES(SELF,DISTANCE,AGE,GENDER)IF DISTANCE >300 20 RS PER KM . IF DIS BETN 100 TO 300 15 RS
#PER KM . ELSE 13 RS , IF AGE LESS THAN 12 PROVIDE 50% DISSCOUNT , IF GENDER = FEMALE 10% DISCOUNT.
class traveller:
    def showdetail(self,id,name,city):
        print(id)
        print(name)
        print(city)
    def charges(self,distance,age,gender):
        print("travelling diatance = ",distance)
        print("Age of the traveller",age)
        print("gender of the traveller",gender)
        sum=0
        if distance>=300:
            sum=distance*20
        elif distance>100 and distance<300:
            sum=distance*15
        else:
            sum=distance*13
        print("total charges without dissscount",sum)
        dis=0
        if age<12:
            dis=sum*12/100
            sum=sum-dis
        print("disscount for childes",dis)
        print("Total charges",sum)
        dis1=0
        if gender=='female':
            dis1=dis*10/100
            sum=sum-dis1
        print("disscount for female",dis1)
        print("total charges",sum)
obj=traveller()
id=int(input("Enter the id"))
name=input("Enter the passenger name")
city=input("Enter the city")
distance=int(input("Enter the distance u have to travvel"))
age=int(input("Enter your age"))
gender=input("(male/female)")
obj.showdetail(id,name,city)
obj.charges(distance,age,gender)
