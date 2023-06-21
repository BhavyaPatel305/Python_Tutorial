from multipledispatch import dispatch
class Amazone():
    
    @dispatch(str)
    def product(self,pname):
        print("produc called with product name",pname)

    @dispatch(str,int)
    def product(self,pname,price):
        print("produc called with product name and price",pname,price)
        
    @dispatch(str,int)
    def product(self,n,p):
        print("produc called with product name and price.....")        
    
    @dispatch(int,str)
    def product(self,price,pname):
        print("produc called without param price and product name")
    
    
    
    @dispatch(int)
    def product(self,price):
        print("produc called int price")
    
    @dispatch(float)
    def product(self,price):
        print("produc called float price")
        

a = Amazone()
#a.product("mobile")        
a.product("mobile",1000)
a.product(1000,"mobile")
a.product(1000)
a.product(1000.0)
