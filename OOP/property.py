class Employee:
    def __init__(self, name, age, position, salary):#Instance attributes OF the class Employee
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None

    #Give the funtionality to show how they work: Method to demonstrate the usage of the Employee class
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

    def __str__(self):
        return f"{self.name} is {self.age} years old employee. He is a {self.position} with the salary of ${self.salary}"
    
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {self.age},"
            f"{repr(self.position)}, {self.salary})"
         )
     
    @property #decorates and add mor functionality to the attribute, prevent bugs
    def salary(self):
        return self._salary 

    @salary.setter #decorator and the name must match the property name
    def salary(self, salary):
        if salary < 1000:
            raise ValueError("Minimum wage is $1000.")
        self._annual_salary = None  # Reset annual salary cache each time salary is updated 
        self._salary = salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self._salary * 12
        return self._annual_salary

    

    
    
#Creating instances of the Employee class WHICH will have their own attribute values
employee1 = Employee("Alice", 30, "Developer", 80000)
employee2 = Employee("Bob", 45, "Manager", 95000)
employee2.increase_salary(10)  # Increase Bob's salary by 10%
print(employee2)  # Display Bob's information
employee1.salary = 1000
print(employee1.salary)
print(employee1.annual_salary)  

