#wapp number operation with class veriable number and str use constructur to initialize the value and defi
#print info (self) . create another class working with number that extend above class .  with def some oof
#dig (self) . the defination find out sum of degit upto single numeber . create another clas working with string
#(self) that accept a string frop parent class and sort the string in assending order as per charecter.
class num_op:
    num=0
    string=""
    def _init_(self,num,string):
        self.num=num
        self.string=string
    def print_info(self):   
        print("Number ",self.num) 
        print("String ",self.string)
class Working_num(num_op):
    def _init_(self,num,string):
        super()._init_(num,string)
    def sum_of_digit(self):
        n=0
        sum=self.num
        while(sum>10):
            n=sum
            sum=0
            while(n>0):
                temp=n%10
                n=int(n/10)
                sum=sum+temp
        self.num=sum
class Working_str(Working_num):
    def _init_(self,num,string):
        super()._init_(num,string)
    def sort_str(self):
        self.string = ''.join(sorted(self.string))

num=int(input("Enter the number "))
string=input("Enter the string ")
obj=Working_str(num,string)
obj.sum_of_digit()
obj.sort_str()
obj.print_info()
