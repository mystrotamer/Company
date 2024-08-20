
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
        company_with_departments = [company for org in organizations for company in org.companies.values() if company]
        if not company_with_departments:
            print("No companies available to add departments.")
            continue
        department = Department(fake.job())
        # إضافة القسم إلى شركة عشوائية
        random.choice(company_with_departments).add_department(department)

    # إنشاء موظفين وهميين
    for _ in range(num_employees):
        company_with_departments = [company for org in organizations for company in org.companies.values() if company.departments]
        if not company_with_departments:
            print("No departments available to add employees.")
            continue
        employee = Employee(fake.name(), fake.random_int(min=1850, max=7000))
        # اختيار شركة عشوائية
        company = random.choice(company_with_departments)
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

if __name__ == "__main__":
    # توليد البيانات الوهمية
    orgs = generate_fake_data(num_organizations=2, num_companies=2, num_departments=2, num_employees=2)
    # طباعة التفاصيل
    print_organization_details(orgs)

