
from faker import Faker
from organization import Organization
from company import Company
from department import Department
from employee import Employee
import random

def generate_fake_data(num_organizations, num_companies, num_departments, num_employees):
    fake = Faker()

    organizations = []

    # إنشاء منظمات وهمية
    for _ in range(num_organizations):
        org = Organization(fake.company())
        organizations.append(org)

    # إنشاء شركات وهمية
    for _ in range(num_companies):
        company = Company(fake.company())
        # إضافة الشركة إلى منظمة عشوائية
        random.choice(organizations).add_company(company)

    # إنشاء أقسام وهمية
    for _ in range(num_departments):
        department = Department(fake.job())
        # إضافة القسم إلى شركة عشوائية
        random.choice(list(random.choice(organizations).companies.values())).add_department(department)

    # إنشاء موظفين وهميين
    for _ in range(num_employees):
        employee = Employee(fake.name(), fake.random_int(min=1850, max=7000))
        # اختيار شركة عشوائية
        company = random.choice(list(random.choice(organizations).companies.values()))
        # التحقق من أن الشركة تحتوي على أقسام قبل محاولة اختيار قسم
        if company.departments:
            # اختيار قسم عشوائي من الشركة
            department = random.choice(list(company.departments.values()))
            # إضافة الموظف إلى القسم
            department.add_employee(employee)

    return organizations

def print_organization_details(organizations):
    # طباعة تفاصيل كل منظمة
    print("Generated Data:")
    for org in organizations:
        print(f"Organization: {org.name}")
        for company_name, company in org.companies.items():
            print(f"  Company: {company.name}")
            for department_name, department in company.departments.items():
                print(f"    Department: {department.name}")
                for employee_name, employee in department.employees.items():
                    print(f"      Employee: {employee.name}, Salary: {employee.salary}")

def add_data():
    # توليد بيانات وهمية
    orgs = generate_fake_data(num_organizations=2,
                              num_companies=6,
                              num_departments=24,
                              num_employees=120)
    return orgs

if __name__ == "__main__":
    orgs = add_data()
    print_organization_details(orgs)

