# write a python program with class exam having def show detail (self,roll num,
#name,city) create another def calculate (self,exam type,no_of_paper,gender)
# if papertype = oral- 750/p
#if exam type = written -1000/p
#if exam type = practical - 400/p
#if gender = female provide 10% extra charge
# et= exam type ,,, en=roll number
class exam:
    def showdetails(self,rn,name,city):
        print("roll num=",rn,"name=",name,"city",city)
    def fees(self,et,p,g):
        if et=="oral":
            c=750*p
        elif et=="written":
            c=1000*p
        elif et=="practical":
            c=400*p
        if g=="female":
            c+=(20/100)*c
        print("please pay ",c,"rs")
obj=exam()
rn=int(input("Enter roll number "))
name=input("Enter your name")
city=input("Enter your city")
et=input("Select exam type (oral,writen,practical")
p=int(input("Number of papers "))
g=input("select gender (female/male)")
obj.showdetails(rn,name,city)
obj.fees(et,p,g)
