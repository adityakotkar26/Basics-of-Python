# W A P P  WWITH CLASS EMPLOIEE HAVING CLASS VERIABLE ID EMPOIE NAME, DEPARTMENT ,AGE . USE CONSTRUCTER TO ENETIALIZE THE VALUE
#AND DEFINATION PRINT INFO . CREATE ANOTHER CLASS TEM EMPLOIEE WITH CLASS VERIABLE SALARY AND EX[ETENCE
#THE CLASS EXTENDS AMPLOIE CLASS WITH DEFINATION CALCULATE SALARY (SELF)CONDITIONS FOR SALARY CLACULATIONS ARE
#IF EXPERENCE <15 35000 SALARY
#IF EXP BRTN 10 TO 15 20000 SALAY
#ELSE 15000
#CLEATE ANOTHER CLASS PERMENANT EMPLOIEE THAT EXTENDS EMPLOIEE CLASS . WITH CLASS VERIABLE QUALIFICATION
#AND A DEF CAL SALARY (SELF)
# IF QUALIFICATION == POST GRADUATE 35000
# IF QUALIFICATION == GRADUATE BUT NOT ENGEREEING INCLUDED 20000
#ELSE 15000
#IF QUALIFICATION IS ENGERING ALSO EXCEPT WORCKING DAY AND CHARGE 250 PER DAY
#IF EMPLOE AGE >60 (BOTH) EMPLOIEE SALARY IS 18 000 ONLY .
class Employee:
    Id=0
    name=''
    department=''
    age=0
    salary=0
    Qual=''
    
    def _init_(self,Id,name,department,age,Q):
        self.Id=Id
        self.name=name
        self.department=department
        self.age=age
        self.Qual=Q
    def print_info(self):
        print("Employee ID ",self.Id)
        print("Employee Name ",self.name)
        print("Employee department ",self.department)
        print("Employee Age ",self.age)
class TempEmp(Employee):
    salary=0
    Experience=0
    def _init_(self,Id,name,department,age,Exp,Q):
        super()._init_(Id,name,department,age,Q)
        self.Experience=Exp
    def cal_Salary(self):
        if self.Experience>15:
            self.salary=30000
        elif self.Experience<15 and self.Experience>10:
            self.salary=20000
        else:
            self.salary=15000
        print(self.salary)
class PerEmp(Employee):
    salary1=0
    def _init_(Qual):
        self.Qual=Qual
    def cal_salary(self):
        if self.Qual=="post graduate":
            self.salary1=30000
        elif self.Qual=="non engg graduate":
            self.salary1=20000
        else:
            self.salary1=15000
        print(self.salary1)
ID=int(input("Enter the id"))
name=input("Enter the Name")
department=input("Enter the department")
age=int(input("Enter the age"))
Exp=int(input("Enter the Experience"))
Q=input("Enter The Qualification \n1.post graduate \n2 non engg graduate")
obj=TempEmp()
obj.print_info()
obj.cal_Salary()










        
    
