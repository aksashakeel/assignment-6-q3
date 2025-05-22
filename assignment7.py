class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        #public variable
        self._salary = salary   #protected variable
        self.__ssn = ssn        #private variable

emp = Employee("Aqsa", 5000, "1234-567-89")      

print("Public:", emp.name)      #correct
print("Protected:", emp._salary)#coreect
# print("Private:", emp.__ssn)    Error:AttributeError: 'Employee' object has no attribute '__ssn'

print("Private:", emp._Employee__ssn)   #coreect with (name mangling)