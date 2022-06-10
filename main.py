# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Employee:
    def __init__(self, id, com_id, grade):
        self.id = id
        self.grade = grade
        self.com_id = com_id
        self.salary = 0


class HighTech:
    def __init__(self, k):
        self.zero_salary_employees = {}
        self.companies = {x: {} for x in range(k)}

    def hire_employee(self, id, *args):
        self.zero_salary_employees[id] = (Employee(id, *args))

    def salary_increase(self, id, com_id, salary):
        if id in self.zero_salary_employees.keys():
            self.zero_salary_employees[id].salary += salary
            self.companies[self.zero_salary_employees[id].com_id].append(self.zero_salary_employees[id])
            del self.zero_salary_employees[id]
        elif com_id in self.companies.keys():
            if id in self.companies[com_id].keys:
                self.companies[com_id][id].salary += salary

    def remove_employee(self, id):
        if id in self.zero_salary_employees.keys():
            del self.zero_salary_employees[id]
        else:
            for company in self.companies.items():
                if id in company.keys():
                    del company[id]

    def sum_grades(self, com_id, m):
        grades = [x.grade for x in self.companies[com_id]]
        grades.sort()
        return sum(grades[:m])

    def avg_grades(self, com_id, min, max):
        in_range = [x.grade for x in self.companies[com_id] if min <= x <= max]
        return sum(in_range) / len(in_range)

    def bump_grades(self, grade):
        for company in self.companies.items():
            for employee in company.items():
                employee.grade += grade
        for employee in self.zero_salary_employees.items():
            employee.grade += grade


if __name__ == '__main__':

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
