class function:
    def __init__(self,var1,var2):
        self.var1=var1
        self.__var2=var2
    def update(self,var1):
        self.var1=var1
        self.__display()
    def __display(self):
        print("value of var1",self.var1)
        print("Value of var2",self.__var2)
obj=function(10,20)
obj.update(30)
obj.function__display(self)
