class Employee:

    employee_nr = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.employee_nr +=1

    def fullname(self):
        return '{} {} {}'.format(self.first, self.last, self.pay)

    def applay_raise(self):
        self.pay = int(self.pay * self.raise_amount)


def main():
    emp1 = Employee('Denis', 'Feier', 3000)
    emp2 = Employee('Sergiu', 'Radu', 3000)

    print(emp1.fullname())
    print(emp2.fullname())
    print(Employee.raise_amount)
    print(emp1.raise_amount)
    print(emp2.raise_amount)
    print("\n change_raise:")
    emp1.raise_amount = 1.09 #raise_amount devine camp al intantei corespunzatoare lui emp1 si isi modifica valuarea
    print(Employee.raise_amount)
    print(emp1.raise_amount)
    print(emp2.raise_amount)
    print("\napplay_raise:")
    emp1.applay_raise()
    emp2.applay_raise()
    print(emp1.fullname())
    print(emp2.fullname())


if __name__ == '__main__':
    main()
