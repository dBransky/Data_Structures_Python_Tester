# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import test_gen


class Employee:
    def __init__(self, id, grade):
        self.id = id
        self.grade = grade
        self.salary = 0
        self.salary_id = self.salary + self.id


class Fail(Exception):
    pass


class Invalid(Exception):
    pass


class HighTech:

    def __init__(self, k, out_file):
        self.k = k
        self.companies = {x: {} for x in range(1, int(k) + 1)}
        self.company_vals = {x: x for x in range(1, int(k) + 1)}
        self.deleted_companies = {}
        self.company_hierarchy = {x: [] for x in range(1, int(k) + 1)}
        out_file.write('Init done.\n')

    def add_employee(self, id, com_id, grade):
        if id <= 0 or com_id <= 0 or com_id > self.k or grade < 0:
            raise Invalid()
        for comapny in list(self.companies.values()):
            if id in comapny.keys():
                raise Fail()
        while com_id in self.deleted_companies:
            com_id = self.deleted_companies[com_id]
        self.companies[com_id][id] = (Employee(id, grade))
        return 'SUCCESS'

    def salary_increase(self, id, salary):
        if salary <= 0 or id <= 0:
            raise Invalid()
        for company in list(self.companies.values()):
            if id in company.keys():
                company[id].salary += salary
                return 'SUCCESS'
        raise Fail()

    def remove_employee(self, id):
        if id <= 0:
            raise Invalid()
        for company in list(self.companies.values()):
            if id in company.keys():
                del company[id]
                return 'SUCCESS'
        raise Fail()

    def acquire_company(self, acq_id, target_id, factor):
        while acq_id in self.deleted_companies:
            acq_id = self.deleted_companies[acq_id]
        while target_id in self.deleted_companies:
            target_id = self.deleted_companies[target_id]
        if target_id <= 0 or acq_id > self.k or acq_id <= 0 or factor <= 0 or target_id == acq_id or target_id > self.k:
            raise Invalid()
        self.companies[acq_id].update(self.companies[target_id])
        self.deleted_companies[target_id] = acq_id

        self.company_vals[acq_id] += factor * self.company_vals[target_id]
        for company in self.company_hierarchy[acq_id]:
            self.company_vals[company] += factor * self.company_vals[target_id]
        self.company_hierarchy[acq_id].extend(self.company_hierarchy[target_id])
        self.company_hierarchy[acq_id].append(target_id)

        del self.companies[target_id]
        return 'SUCCESS'

    def promote_employee(self, id, grade):
        if id <= 0:
            raise Invalid()
        for company in list(self.companies.values()):
            if id in company.keys():
                if grade > 0:
                    company[id].grade += grade
                return 'SUCCESS'
        raise Fail()

    def sum_grades(self, com_id, m):
        if m <= 0 or com_id < 0 or com_id > self.k:
            raise Invalid()
        if com_id == 0:
            emp = [emp for comp in list(self.companies.values()) for emp in comp.values() if emp.salary != 0]
            emp.sort(key=lambda x: (x.salary, x.id), reverse=True)
            grades = [x.grade for x in emp]
            if m <= len(grades):
                return self.format_print((sum(grades[:int(m)])), False, True)
            raise Fail()
        while com_id in self.deleted_companies:
            com_id = self.deleted_companies[com_id]
        emp = [emp for emp in self.companies[com_id].values() if emp.salary != 0]
        emp.sort(key=lambda x: (x.salary, x.id), reverse=True)
        grades = [x.grade for x in emp]
        if m <= len(grades):
            return self.format_print((sum(grades[:int(m)])), False, True)
        raise Fail()

    def avg_grades(self, com_id, min, max):
        if min < 0 or max < 0 or min > max or com_id < 0 or com_id > self.k:
            raise Invalid()
        if com_id == 0:
            in_range = [emp for comp in list(self.companies.values()) for emp in comp.values() if
                        min <= emp.salary <= max]
            in_range.sort(key=lambda x: (x.salary, x.id), reverse=True)
            grades = [x.grade for x in in_range]
            if 0 != len(grades):
                return self.format_print((sum(grades) / len(grades)), True, False)
            raise Fail()
        while com_id in self.deleted_companies:
            com_id = self.deleted_companies[com_id]
        in_range = [emp for emp in self.companies[com_id].values() if min <= emp.salary <= max]
        in_range.sort(key=lambda x: (x.salary, x.id), reverse=True)
        grades = [x.grade for x in in_range]
        if 0 != len(grades):
            return self.format_print((sum(grades) / len(grades)), True, False)
        raise Fail()

    def bump_grades(self, min, max, grade):
        if grade <= 0 or min > max:
            raise Invalid()
        for company in list(self.companies.values()):
            for employee in company.values():
                if min <= employee.salary <= max:
                    employee.grade += grade
        return 'SUCCESS'

    def quit(self, *args):
        return 'done.'

    def company_value(self, id):
        if id <= 0 or id > self.k:
            raise Invalid()
        return self.format_print((float(self.company_vals[id])), True, False)

    def format_print(self, line, _, whole):
        if whole:
            return str(line)
        else:
            if str(line).split('.')[1][0] == '9' and float('0.'+str(line).split('.')[1][1:]) > 0.5:
                return str(round(line, 0))
            return str(round(line, 1))


if __name__ == '__main__':
    funcs = {'Init': HighTech, 'AddEmployee': HighTech.add_employee, 'EmployeeSalaryIncrease': HighTech.salary_increase,
             'PromoteEmployee': HighTech.promote_employee, 'AverageBumpGradeBetweenSalaryByGroup': HighTech.avg_grades,
             'SumOfBumpGradeBetweenTopWorkersByGroup': HighTech.sum_grades, 'AcquireCompany': HighTech.acquire_company,
             'Quit': HighTech.quit, 'RemoveEmployee': HighTech.remove_employee, 'CompanyValue:': HighTech.company_value}
    lines = 50000
    for i in range(1):
        test_gen.TestGen(f'in{i}.txt', lines)
    for i in range(1):
        out_file = open(f'out{i}.txt', 'w+')
        with open(f'in{i}.txt') as file:
            lines = file.readlines()
            lines = [line.strip('\n') for line in lines]
            lines = [(line.split(' ')[0], funcs[line.split(' ')[0]],
                      list(map(lambda x: float(x), list(filter(lambda a: a != '', line.split(' ')[1:])))))
                     for line in lines]
            high_tech = None
            num = 0
            for line in lines:
                try:
                    if high_tech is None:
                        out = high_tech = line[1](*line[2], out_file)
                    else:
                        out = line[1](high_tech, *line[2])
                        if line[0] == 'CompanyValue:' or line[0] == 'Quit':
                            out_file.write(f'{line[0]} {out}\n')
                        else:
                            out_file.write(f'{line[0]}: {out}\n')
                except Fail:
                    if line[0] == 'CompanyValue:':
                        out_file.write(f'{line[0]} FAILURE\n')
                    else:
                        out_file.write(f'{line[0]}: FAILURE\n')
                except Invalid:
                    if line[0] == 'CompanyValue:':
                        out_file.write(f'{line[0]} INVALID_INPUT\n')
                    else:
                        out_file.write(f'{line[0]}: INVALID_INPUT\n')
        print(f'file {i} generated')
        out_file.close()
