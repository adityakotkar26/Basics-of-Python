# WRITE AP P TO ACCEPT A NUMBER FROM THE USER AND PRINT THE AMSTRONG NUMBER FROM
#1 TO N NUMBER USING TRICAGE BLOCK 33
class amstrong:
    def find (self):
        try:
            n=int(input("Enter the number "))
            for i in range (1,n+1):
                r=0
                a=0
                temp=i
                while i>0:
                    r=i%10
                    a+=r*r*r
                    i=i//10
                if temp==a:
                    print(a)
        except ValueError:
            print("bhau number takaychay letter nahi")
        except Exception:
            print("chukla program")
        finally:
            print("Thank you")
obj=amstrong()
obj.find()
