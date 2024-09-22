#wapp with class student having class veriable roll number , name , department use constructer to
# initialize the class veriable and def show detail create another class internal marks that extends
#above class with class veriable python internal marks and def print internal marks . create another
#class external exam that extends inter nal exam . with class veriable python internal marks and defination
# print inter nal marks create amother class result that extends external exam and def calculate result
# with folowing condition:
# if inter nal marks less than 12 stu fail .
# if external marks less tha 28 student fail
# make a total of inter and external exam and find out grade with following condition :
#if total > 70 A+ grade if total betn 60 to 70 a grade . if total bets 50 to 60 B grade . if total betn
# 40 to 50 c grade . 30 to 40 d else fail .
class student:
    roll=0
    name=" "
    dept=" "
    def __init__(self,roll,name,dept):
        self.roll=roll
        self.name=name
        self.dept=dept
    def info(self):
        print("student roll number :",self.roll)
        print("student name :",self.name)
        print("student department:",self.dept)
        
class internal(student):
    imarks=0
    def __init__(self,roll,name,dept,imarks):
        super().__init__(roll,name,dept)
        self.imarks=imarks
    def print_imarks(self):
        print("Students internal marks",self.imarks)
        
class external(internal):
    emarks=0
    def __init__(self,roll,name,dept,imarks,emarks):
        super().__init__(roll,name,dept,imarks)
        self.emarks=emarks
    def print_emarks(self):
        print("Student Extrnal marks",self.emarks)
        
class Result(external):
    def __init__(self,roll,name,dept,imarks,emarks):
        super().__init__(roll,name,dept,imarks,emarks)
    def result(self):
        if self.imarks<12:
            print("FAIL")
        if self.emarks<28:
            print("FAIL")
        total=self.imarks+self.emarks
        print("Total marks : ",total)
        if total >= 70:
            print("A+ grade")
        elif total >=60 and total<70:
            print("A grade")
        elif total >=50 and total<60:
            print("B grade")
        elif total >= 40 and total<50:
            print("C grade")
        else :
            print("FAIL")
roll=int(input("Enter your roll rumber"))
name=input("Enter student name ")
dept=input("Enter the students depatment ")
imarks=int(input("Enter the Students internal marks"))
emarks=int(input("Enter the student external marks"))
obj=Result(roll,name,dept,imarks,emarks)
obj.info()
obj.print_imarks()
obj.print_emarks()
obj.result()




















