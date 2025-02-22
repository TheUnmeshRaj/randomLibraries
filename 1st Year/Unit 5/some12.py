class Company:
    def __init__(self):
        self._project="NLP"
class Employee(Company):
    def __init__(self,name):
        self.name=name
        super().__init__()
    def show(self):
        print(self.name,"is working on",self._project)

c= Employee("Jessa")
c.show()

print("project is",c._project)
        