class Family:
    # Constructor - parameterized  
    members=""
    def __init__(self, count):  
        print("This is parametrized constructor")  
        self.members = count
    def show(self):  
        print("No. of members is: n", self.members)  
        
object = Family(10)  
object.show()