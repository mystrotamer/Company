
class Company:

    def __init__(self, name):
        self.name = name
        self.departments = {}

    def add_department(self, department):
        if department.name in self.departments:
            print(f"Department '{department.name}' already exists.")
        else:
            self.departments[department.name] = department

    def remove_department(self, department):
        if department.name in self.departments:
            del self.departments[department.name]
        else:
            print(f"Department '{department.name}' not found.")

    def __str__(self):
        department_list = "\n  ".join(str(dept) for dept in self.departments.values())
        return (f"Company Name: {self.name}\n "
                f"Departments:\n  {department_list if department_list else 'No Departments'}")

    def __repr__(self):
        return f"Company('{self.name}')"
