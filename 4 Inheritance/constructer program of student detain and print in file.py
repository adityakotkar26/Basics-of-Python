#write a python program with class course having class variables course id,course name,duration,fees.
#use constructor to initialize the value and the method or def printinfo.create another def calculate
#fees(self,percentage) if %.70 10%schlorship on fees,if % bet 60-70 8% schlorship else 5%.If course
#type =programing provide 2% extra disc also add 3% exam charges,0.5% certificate charges and if all
#data is valid store in exam.txt file.also handle the exception with foll. cond
#1]fees amt less than0
#2]course name programming ms-cit,tally,etc.
#if it is not found throw and exception
class cource:
    cid=0
    name=" "
    duration=0
    fees=0
    def __init__(self,cid,name,duration,fees):
        self.cid=cid
        self.name=name
        self.duration=duration
        self.fees=fees
    def calculate(self,percent):
        if percent>=70:
            paid=self.fees*10/100
        elif percent>=60 and percent<70:
            paid=self.fees*8/100
        else:
            paid=self.fees*5/100
        print("discount on exam fees is :",paid)
        self.fees=self.fees-paid
        print("Total fees with schorship pay",self.fees)
        if self.name=="programing":
            p=total*2/100
            self.fees=self.fees-p
        print("total fees with the dissocunt of programing",self.fees)
        e=self.fees*3/100
        print("exam charges",e)
        c=self.fees*0.5/100 
        print("certificate charges",c)
        self.fees=self.fees+e+c
        print("Final payment",self.fees)
    def file(self):
        fp=open("studentinformation.txt","a+")
        print(" ")
        fp.write(str(self.cid))
        print(" ")
        fp.write(self.name)
        print(" ")
        fp.write(str(self.duration))
        print(" ")
        fp.write(str(self.fees))
cid=int(input("Enter student id:"))
name=input("Enter the student name")
duration=int(input("Enter the duration of cource"))
fees=int(input("Enter the fees"))
percent=float(input("Enter the percentage of student:"))
obj=cource(cid,name,duration,fees)
obj.calculate(percent)
obj.file()

            




        
            
