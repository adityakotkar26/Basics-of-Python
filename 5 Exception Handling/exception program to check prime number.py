# write a exception handling prog to accept a number and checkthe number is
#primeor not and aso print next prime number also handle appropriate exception
class prime:
    def find(self):
        try:
            n=int(input("Enter the number"))
            for i in range(2,n):
                if n%i==0:
                    flag=1
                    break
                else:
                    flag=0
            if flag==1:
                print("not a prime number")
            else:
                print("prime number")
            for i in range (n+1,n+10):
                for j in range (2,i):
                    if i%j==0:
                        flag=1
                        break
                    else:
                        flag=0
                if flag==0:
                        print("next prime number=",i)
                        break
        except ValueError:
            print("bhava number tak letter nahi")
        except Exception :
            print("bhau program chukla")
        finally:
            print("thank you")
obj=prime()
obj.find()
