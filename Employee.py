
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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, str_emp):
        first, last, pay = str_emp.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_working(data):
        if data.weekday() == 5 or data.weekday() == 6:
            return False
        else:
            return True


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

    print('Se aplica metoda class set_raise_amount:')
    Employee.set_raise_amount(1.5)

    print(Employee.raise_amount)
    print(emp1.raise_amount) # pt emp1 ii inca camp instance
    print(emp2.raise_amount)

    print("Rezultatul unui constructor alternativ:")
    print(Employee.from_string('Mircea-Mosul-1000').fullname())
    print("Static methode:")


if __name__ == '__main__':
    main()
