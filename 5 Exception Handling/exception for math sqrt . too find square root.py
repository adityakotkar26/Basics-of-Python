# write a python program to accept the number from the user and print the square
# root of given number. if it is not perfect then throw invalid square root exception
import math
class nonperfect(Exception):
    def __init___(self):
        print("Error")
class trial:
    def getnum(self):
        try:
            num=int(input("Enter the number"))
            ans=math.sqrt(num)
            a=ans
            if ans!=int(a):
                raise nonperfect()
            else:
                print("",ans)
        
            
        except nonperfect as e:
            print("Invalid number")
                                                       
                    
        finally:
            print("thank you")
obj=trial()
obj.getnum()

           
