#WRITE A PROGRAM WITH CLASS STUDENT WITH DEF GET INFO (SELF,ID,NAME,DEPARTMENT) CREATE ANOTHER DEF
#(EXAM CHARGES(SELF,NUMBER OF Paper , EXAM TYPE) IF EXAM TYPE IS ORAL 150 RS PER PAPER , IF IT IS RETUEN
#200 RS PER PAPER , EXAM TYPE IS ONLINE 600 RS PER PAPER .
class student:
    def getinfo(self,id1,name,dept):
        print(id1,name,dept)
    def exam (self,no_p,type1):
        sum=0
        if type1=='oral':
            sum=no_p*150
        elif type1=='writen':
            sum=no_p*200
        elif type1=='online':
            sum=no_p*600
        else:
            print("Mode not available")
        print("please paid",sum)
obj=student()
id1=int(input("Enter the student id :"))
name=input("Enter the student name:")
dept=input("Enter the dept:")
no_p=int(input("Enter the number of paper"))
type1=input("Select exam type (oral,writen,online):")
obj.getinfo(id,name,dept)
obj.exam(no_p,type)
        
