# WRITE A PYTHON PROGRAM TO ACCEPT A NUMBER AND CHECK IT IS AMSTRONG OR NOT IF THE AMSTRONGNUMBER FOUND
#PRINT THE NUMBER IS AMSTRONG AND ALSO PRINT THE NEXT AMSTRONG NUMBER . IF NON AMSTRONG NUMBER
#FOUND THROW INVALID NUMBER EXCEPTION
class amstrong(Exception):
    def __init__(self):
        print("error")
class trial:
    def find(self,num):
        try:
            temp=num
            sum=0
            while temp!=0:
                n=temp%10
                sum=sum+n*n*n
                temp=temp//10
            if num==sum:
                print("Number is amstrong")
                for i in range(num+1,1000):
                    sum=0
                    temp=i
                    while temp!=0:
                        n=temp%10
                        sum=sum+n*n*n
                        temp=temp//10
                    if i==sum:
                        print("Next amstrong",i)
                        break
            else:
                raise amstrong()
        except amstrong as e:
            print("number is not amstrong")
        except Exception as e1:
            print("bhau program chukla")
        finally:
            print("thank you")
obj=trial()
n=int(input("Enter the number "))
obj.find(n)
