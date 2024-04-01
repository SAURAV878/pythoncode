class Employee:

    def __init__(self, name, project, salary):
        self.name = name #public member(accessible within or autside of a class)
        self._project = project #procted member(accessible within the class and it's sub-classes)
        self.__salary = salary #privated number (accessible only within a class)
    

    def show(self):
        print("Name : ", self.name)


emp = Employee('madhav', 'Xavier', 1000)
emp.show()
print(emp.name)
print(emp._project)
print(emp._Employee__salary)        