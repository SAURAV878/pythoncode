#inhertiance = the process of inheritaing the process of teh parent class

class Person:
    def person_info(self, name, age):
        print('Iniside Person Class')
        self.name = name
        print('Name : ', name, 'Age : ',age)

class Company:
    def company_info(self, company_name, location):
        print("Inisde Company Class")
        print('Name: ', company_name, 'Location: ',location)       


class Employee(Person, Company):
    def employee_info(self,salary,skill):
        super().person_info('Saurav', 20)
        print('Inside Employee class')
        print('Salary: ', salary, 'skill: ',skill)

emp = Employee()

emp.person_info("Arjun", 25)

emp.employee_info(1200,'Machine')
