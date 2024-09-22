# WRITE A PYTHON PROGRAM WITH CLASS STRINGOPERATION WITH DEF FINDLARGEST(SELF,STR)
#def countvowels(self,str)
class stroperation:
    def largest(self,str):
        ans=str.split()
        larg=ans[0]
        for i in range (len(ans)):
            if len(larg)<len(ans[i]):
                larg=ans[i]
        print(larg)
    def cvowels(self,str):
        count=0
        for i in range (len(str)):
            if(str[i] == 'a' or
               str[i] == 'A' or
               str[i] == 'e' or
               str[i] == 'E' or
               str[i] == 'i' or
               str[i] == 'I' or
               str[i] == 'o' or
               str[i] == 'O' or
               str[i] == 'U' or
               str[i] == 'u' ):
                count=count+1
        print(count)
obj=stroperation()
str=input("Enter the string")
obj.largest(str)
obj.cvowels(str)
