# WRITE A PYTHON PROG WITH CLASS EMPLOYE WITH DEFINATION GETDETAIL(SELF,ID,NAME,
#DEPARTMENT) CREATE ANITHER CLASS TEMPORARY EMPLOIE THAT EXTEND EMPLOIE CLASS
#WITH DEFINATION .CALCUATE SALARY (SELF,QUALIFICATION,NO OF MONTHS )CONDITION FOR
#SALARY CALCULATIONS ARE
#IF qUALIFICALTION = DIPLOMA -- 10000 RS/M
#IF QUALIFICALTION = DEGREE  -- 15000 RS/M
#ELSE                        -- 8000  RS/M
#CREATE ANOTHER CLASS PERMANT EMPLOIEE THAT EXTENDS EMPLOIEE CLASS WITH DEF CALCULATE SALARY
#(SELF,EXPERIANCE,NO OF MONTH) CONDITION FOR SALLARY CALCULATIONS ARE:-
#IF EXPERIANCE > 5 -- 10000R/M
#IF eXPERIANCE > 3 AND <5 -- 8000 RS/M
#ELSE 5000 RS/M
class emp:
    def getdetails(self,id,name,department):
        print("Id=",id,"name=",name,"department=",department)
class temp_emp(emp):
    def cal_salary (self,q,no_months):
        if q=="DIPLOMA":
            r=10000*no_months
        elif q== "DEGREE":
            r=15000*no_months
        else:
            r=8000*no_months
        print("Your salary=",r,"RS")
class per_emp(emp):
    def cal_salary(self,exp,no_m):
        if exp>=5:
            x=10000*no_m
        elif exp>=3 and exp<5:
            x=8000*no_m
        else:
            x=5000*no_m
        print("your salary=",x,"RS")
id=int(input("Enter your id"))
name=input("Enter the name")
department=input("Enter your department ")
emp_type=input("select department TEMORARY OR NOT ")
if emp_type=="temp":
    obj1=temp_emp()
    q=input("Enter qualification (DIPLOMA/DEGREE)")
    no_months=int(input("Enter the duration of working in years"))
    obj1.getdetails(id,name,department)
    obj1.cal_salary(q,no_months)
else:
    obj2=per_emp()
    exp=int(input("Enter the Exeperiance in years"))
    no_m=int(input("Enter the Experiance in months"))
    obj2.getdetails(id,name,department)
    obj2.cal_salary(exp,no_m)

















            
