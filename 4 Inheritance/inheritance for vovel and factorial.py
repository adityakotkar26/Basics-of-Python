# write a python program with class math operation with def calculate factorial (self, num). create another
#class string operation that excends above class . with defination count vovels (self,str) .
class math:
    def factorial(self,num):
        f=1
        for i in range(1,num+1):
            f=f*i
        print("factorial",f)
class string_operation(math):
    def cnt_vovels(self,str):
        count=0
        for i in range(len(str)):
            if str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u":
                count=count+1
        print("the  vovels from given string",count)
obj=string_operation()
num=int(input("Enter the number"))
obj.factorial(num)
str=input("Enter the sting")
obj.cnt_vovels(str)
