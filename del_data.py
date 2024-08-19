
from add_data import add_data, print_organization_details
from organization import Organization
from company import Company
from department import Department
from employee import Employee
import random

def remove_random_data(organizations):
    # حذف منظمة عشوائية
    if organizations:
        org_to_remove = random.choice(organizations)
        organizations.remove(org_to_remove)
        print(f"Removed Organization: {org_to_remove.name}")

    # حذف شركة عشوائية من كل منظمة
    for org in organizations:
        if org.companies:
            company_to_remove = random.choice(list(org.companies.values()))
            org.remove_company(company_to_remove)
            print(f"Removed Company: {company_to_remove.name} from Organization: {org.name}")

    # حذف قسم عشوائي من كل شركة
    for org in organizations:
        for company in org.companies.values():
            if company.departments:
                department_to_remove = random.choice(list(company.departments.values()))
                company.remove_department(department_to_remove)
                print(f"Removed Department: {department_to_remove.name} from Company: {company.name}")

    # حذف موظف عشوائي من كل قسم
    for org in organizations:
        for company in org.companies.values():
            for department in company.departments.values():
                if department.employees:
                    employee_to_remove = random.choice(list(department.employees.values()))
                    del department.employees[employee_to_remove.name]
                    print(f"Removed Employee: {employee_to_remove.name} from Department: {department.name}")

if __name__ == "__main__":
    orgs = add_data()
    print("Before removal:")
    print_organization_details(orgs)
    remove_random_data(orgs)
    print("\nAfter removal:")
    print_organization_details(orgs)


