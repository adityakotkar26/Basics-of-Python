#WRITE A PYTHON PROG TO ACCEPT THE ARRAY OF 15 ELEMENTS ADCOUNT THE AUVARENCE OF DUBLICATE ELEMENTS .IF
# IT IS >3 THROW USER DEFINE EXCEPTION ADDITIONAL DUBLICATE ELEMENT
class DublicateException(Exception):
    def __init__(self):
        print("Error")
class trial:
    try:
        import array as arr
        num=arr.array("i",[])
        size=int(input("Enter the size of array"))
        n=int(input("Enter your choice"))
        count=0
        for i in range (size):
            a=int(input("Enter the number "))
            num.append(a)
            for i in range(size):
                if num[i]==a:
                    count=count+1
                if count>3:
                    raise DublicateException()
                else:
                    print("occurance=",count)
    except dublicateException as e:
        print("greater than 3")
    finally:
        print("Thank you ")
        

