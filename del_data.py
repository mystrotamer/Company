
from add_data import generate_fake_data, print_organization_details
from organization import Organization
from company import Company
from department import Department
from employee import Employee
import random

def remove_random_data(organizations):
    if not organizations:
        print("No organizations to remove from.")
        return

    # اختيار منظمة عشوائية
    org = random.choice(organizations)

    if not org.companies:
        print(f"Organization '{org.name}' has no companies to remove.")
        organizations.remove(org)
        print(f"Removed Organization: {org.name}")
        return

    # اختيار شركة عشوائية داخل المنظمة
    company = random.choice(list(org.companies.values()))

    if not company.departments:
        print(f"Company '{company.name}' has no departments to remove.")
        org.remove_company(company)
        print(f"Removed Company: {company.name} from Organization: {org.name}")
        return

    # اختيار قسم عشوائي داخل الشركة
    department = random.choice(list(company.departments.values()))

    if not department.employees:
        print(f"Department '{department.name}' has no employees to remove.")
        company.remove_department(department)
        print(f"Removed Department: {department.name} from Company: {company.name}")
        return

    # حذف موظف عشوائي من القسم
    employee = random.choice(list(department.employees.values()))
    department.remove_employee(employee)
    print(f"Removed Employee: {employee.name} from Department: {department.name}")

    # حذف القسم إذا أصبح فارغًا
    if not department.employees:
        company.remove_department(department)
        print(f"Removed Department: {department.name} from Company: {company.name}")

    # حذف الشركة إذا أصبحت فارغة
    if not company.departments:
        org.remove_company(company)
        print(f"Removed Company: {company.name} from Organization: {org.name}")

    # حذف المنظمة إذا أصبحت فارغة
    if not org.companies:
        organizations.remove(org)
        print(f"Removed Organization: {org.name}")

if __name__ == "__main__":
    # توليد البيانات الوهمية
    orgs = generate_fake_data(num_organizations=2, num_companies=5, num_departments=11, num_employees=33)
    # طباعة التفاصيل قبل الحذف
    print("Before random removal:")
    print_organization_details(orgs)
    
    # حذف بيانات عشوائية
    remove_random_data(orgs)
    
    # طباعة التفاصيل بعد الحذف
    print("\nAfter random removal:")
    print_organization_details(orgs)


