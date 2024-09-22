#write a python program class student def get info (self,id name,age) create another  def calculate avegrage
#m1,m2,m3 def calculate totale avg and grade create 2 objectcompare 2 object with eachother if obj are matched
#write in obj.txt
class student:
    def grade(self,m1,m2,m3):
        a=m1+m2+m3/3
        if a>=70:
            print("A+ Grade")
        elif a>=60 and a<70:
            print("A grade")
        elif a>=50 and a<60:
            print("B grade")
        else:
            print("fail")
    def info(self,id ,name,age):
        print(self,id ,name,age)
    
obj=student()
id=int(input("id"))
name=input("name")
age=int(input("age"))
m1=int(input("Enter the marks of m1"))
m2=int(input("Enter the marks of m2"))
m3=int(input("Enter the marks of m3"))
obj.grade(m1,m2,m3)
obj.info(id,name,age)

            
    

