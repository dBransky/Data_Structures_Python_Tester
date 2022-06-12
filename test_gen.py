import random


class TestGen:
    def __init__(self, path, lines):
        self.funcs = [('AddEmployee', self.rand_test_add), ('AddEmployee', self.rand_test_add),
                      ('AddEmployee', self.rand_test_add), ('AddEmployee', self.rand_test_add),
                      ('EmployeeSalaryIncrease', self.rand_test_sal_increase),
                      ('PromoteEmployee', self.rand_test_promote),
                      ('AverageBumpGradeBetweenSalaryByGroup', self.rand_test_avg),
                      ('SumOfBumpGradeBetweenTopWorkersByGroup', self.rand_test_sum),
                      ('AcquireCompany', self.rand_test_acq),
                      ('RemoveEmployee', self.rand_test_rem),
                      ('CompanyValue', self.rand_test_val),
                      ('BumpGradeToEmployees', self.rand_test_bump)
                      ]

        self.companies = random.randint(0, 50)
        self.total_emp = 0
        with open(path, 'w+') as file:
            file.write(f'Init {self.companies}\n')
            for i in range(lines):
                func = random.randint(0, len(self.funcs) - 1)
                file.write(self.funcs[func][1]() + '\n')
            file.write('Quit')

    def rand_test_bump(self):
        return f'BumpGradeToEmployees  {str(random.randint(-1, 1100000000))} {str(random.randint(1000000000, 2100000000))} {str(random.randint(-1, 2100000))}'

    def rand_test_add(self):
        self.total_emp += 1
        return f'AddEmployee {str(random.randint(-1, 10000))} {str(random.randint(-1, self.companies + 1))}  {str(random.randint(-1, 2100000))}'

    def rand_test_sal_increase(self):
        return f'EmployeeSalaryIncrease {str(random.randint(-1, 10000))} {str(random.randint(-1, 2100000))}'

    def rand_test_promote(self):
        return f'PromoteEmployee {str(random.randint(-1, 10000))} {str(random.randint(-1, 2100000))}'

    def rand_test_avg(self):
        return f'AverageBumpGradeBetweenSalaryByGroup  {str(random.randint(-1, self.companies + 1))} {str(random.randint(-1, 1000000))} {str(random.randint(1000000, 2100000))}'

    def rand_test_sum(self):
        return f'SumOfBumpGradeBetweenTopWorkersByGroup  {str(random.randint(-1, self.companies + 1))} {str(random.randint(-1, int((self.total_emp + 1)/((self.companies)+1))))}'

    def rand_test_acq(self):
        return f'AcquireCompany {str(random.randint(-1, self.companies + 1))} {str(random.randint(-1, self.companies + 1))} {str(round(random.uniform(-0.1, 10), 5))}'

    def rand_test_rem(self):
        return f'RemoveEmployee {str(random.randint(-1, 10000))}'

    def rand_test_val(self):
        return f'CompanyValue: {str(random.randint(-1, self.companies + 1))}'
