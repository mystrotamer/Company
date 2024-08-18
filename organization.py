
class Organization:
    def __init__(self, name):
        self.name = name
        self.companies = {}

    def add_company(self, company):
        if company.name in self.companies:
            print(f"Company '{company.name}' already exists.")
        else:
            self.companies[company.name] = company

    def remove_company(self, company):
        if company.name in self.companies:
            del self.companies[company.name]
        else:
            print(f"Company '{company.name}' not found.")

    def __str__(self):
        company_list = ", ".join(self.companies.keys())
        return (f"Organization Name: {self.name}, "
                f"Companies: {company_list if company_list else 'No companies'}")
