
class Department:
    
    def __init__(self, name):
        self.name = name
        self.employees = {}
    
    def add_employee(self, employee):
        if employee.name in self.employees:
            print(f"Employee '{employee.name}' already exists in the department.")
        else:
            self.employees[employee.name] = employee

    def remove_employee(self, employee):
        if employee.name in self.employees:
            del self.employees[employee.name]
        else:
            print(f"Employee '{employee.name}' not found.")
       
    def __str__(self):
        employee_list = "\n    ".join(str(emp) for emp in self.employees.values())
        return (f"Department Name: {self.name}\n "
                f"Employees:\n    {employee_list if employee_list else 'No Employees'}")
