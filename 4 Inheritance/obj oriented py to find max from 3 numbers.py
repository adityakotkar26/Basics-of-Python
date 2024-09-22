#WRITE A PYTHON PROGRAM WITH CLASS MAX USED TO FIND OUT MAXIMUM NUMBERS FROM THREE
#NUMBERS AND ARRAY FIND MAX CLASS NAME MAX WITH DEFINATION DEF PRINT MAX (SELF ,A,
#B,C) DEF (SELF,A[])
class maximum:
    def max (self,a,b,c):
        if a>b and a>c:
            print("max is=",a)
        elif b>a and b>c:
            print("max is = ",b)
        else:
            print("max is =",c)
    def arraymax(self,arr):
        for i in range (3):
            for j in range (i+1,3):
                if arr [i]<arr[j]:
                    arr[j],arr[i]==arr[i],arr[j]
                    print("max in array=",arr[0])
obj=maximum()
a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
c=int(input("Enter the third number "))
import array as array
arr=array.array("i",[])
for i in range(3):
    x=int(input("Element of array element"))
    arr.append(x)
obj.max(a,b,c)
obj.arraymax(arr)
