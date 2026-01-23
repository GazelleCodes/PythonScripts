class Employee:
    company_name = "Pluralsight"
    def __init__(self, name, employee_id, email):
      self.name = name
      self.employee_id = employee_id
      self.email = email

    def get_contact_info(self):
      return f"{self.name} ({Employee.company_name}) can be reached at {self.email}"

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, email, salary):
        super().__init__(name, employee_id, email)
        self.salary = salary


    def is_high_earner(self):
        if self.salary >= 100000:
            return True
        else:
            return False
 
class Intern(Employee):
   def __init__(self, name, employee_id, email, school):
       super().__init__(name, employee_id, email)
       self.school = school
   
   def get_contact_info(self):
        return f"{self.name} (from {self.school} at {Employee.company_name}) can be reached at {self.email}"
   


# Creating instances of FullTimeEmployee and Intern classes
if __name__ == "__main__":
    full_time_emp = FullTimeEmployee("John Doe", "FT123", "john.doe@pluralsight.com", 120000)
    intern = Intern("Jane Smith", "INT456", "jane.smith@pluralsight.com", "University of Technology")
    employee1 = Employee("Alice", "FT789", "alice@pluralsight.com")


    employees = [full_time_emp, intern, employee1]

    for employee in employees:
        print(employee.get_contact_info())


    for employee in employees:
        if isinstance(employee, FullTimeEmployee):
            if employee.is_high_earner():
                print(f"{employee.name} is a high earner.")
            else:
                print(f"{employee.name} is not a high earner.")
        else:
            print(f"{employee.name} does not have a salary attribute.")

        
    