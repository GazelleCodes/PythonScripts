class Employee:
    def __init__(self, name, age, position, salary):#Instance attributes OF the class Employee
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

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
#Creating instances of the Employee class WHICH will have their own attribute values
employee1 = Employee("Alice", 30, "Developer", 80000)
employee2 = Employee("Bob", 45, "Manager", 95000)
employee2.increase_salary(10)  # Increase Bob's salary by 10%
print(employee2)  # Display Bob's information

