from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current Employees:")
        for emp in self.employees:
            print(f'{emp.fname} {emp.lname}')
        print("---------------")

    def pay_employees(self):
        print("Paying Employees:")
        for emp in self.employees:
            print(f'Paycheck for : {emp.fname} {emp.lname}')
            print(f'Amount: ${emp.calculate_paycheck():,.2f}')
            print("---------------")

def main():
    my_company = Company()

    emp1 = SalaryEmployee('John', 'Doe', 52000)
    emp2 = HourlyEmployee('Jane', 'Smith', 40, 15)
    emp3 = CommissionEmployee('Emily', 'Davis', 58000, 35, 200)
    

    my_company.add_employee(emp1)
    my_company.add_employee(emp2)
    my_company.add_employee(emp3)

    my_company.display_employees()
    my_company.pay_employees()

main()
