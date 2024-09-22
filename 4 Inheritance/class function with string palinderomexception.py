# WRITE A PYTHON PROM WITH CLASS WORKING WITH FIL WITH DEF CHECK EQUALITY(SELF,FNAME,SNAME). THE DEFINATION COMPAIR
#TWO FILES . IF FILES ARE MATCH IT WREETEN CONTAIN MATCHED ELSE DOSE NOT MATCH
#DEF CONVERT CHAR (SELF,FNAME) THE DEFINATION CONVERT FIRST CHARECTER OD EACH NEW LINE IN CAPITAL  LETTER
#EVERY LINE END WITH . SYMBOL
#DEF PRINT PALINDEROM (SELF,FNAME) THE DEFINATIO PRINT THE PALINDEROM WORDS FROM THE FILE . ACCEPT THE
#FILE NAME FROM THE USER . IF THE FILE LENGTH LESS THAN 2 KB THROW INVALID FILE EXCEPTION
class filenotfound(Exception):
    def _init_(self):
        print("Error")

class working_with_file:
    try:
        
        def check_equality(self,fname,sname):
            fp1=open(fname,"r")
            ans1=fp1.read()
            fp2=open(sname,"r")
            ans2=fp2.read()
            if ans1==ans2:
                print("files are same")
            else:
                print("files are notsame")
        def convert_char(self,fname):
            fp1=open(fname,"r")
            ans=fp1.read()
            temp='0'
            for i in range(len(ans)):
                if ans[i]==".":
                    ans[i+1]=ans[i+1].upper()
                print(ans[i])

        def palindrome(self,fname):
            fp1=open(fname,"r")
            ans1=fp1.read()
            ans=ans1.split(" ")
            for i in range(len(ans)):
                temp=ans[i]
                rev = temp[::-1]
                if temp==rev:                                        
                    print(" ",temp)
            num=len(ans)
            num=num*1024
            if num<2048:
                print("length of file",num)
            else:
                print("valid file")
    except filenotfound as e:
        print("file is invalid")
   
obj=working_with_file()
fname=input("Enter the file name1")
sname=input("Enter the file name2")
obj.convert_char(fname)
obj.check_equality(fname,sname)
obj.palindrome(fname)
        
            
        
                    
        
        
        
