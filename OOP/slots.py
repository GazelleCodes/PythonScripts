class Developer:
    __slots__ = ['name', 'age', 'salary', 'framework']#Define allowed attributes to save memory and fasten attribute access. 
    
    def __init__(self, name, age,  salary, framework):#Instance attributes OF the class Employee
        self.name = name
        self.age = age
        self.salary = salary
        self.framework = framework


employee1 = Developer("Alice", 30, 80000, "React")
employee2 = Developer("Bob", 45, 95000 , "Django")