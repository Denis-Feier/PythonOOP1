class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}\n'.format(self.first, self.last, self.email)


def main():
    emp1 = Employee('Denis', 'Feier', 3000)
    emp2 = Employee('Sergiu', 'Radu', 4000)

    print(emp1.fullname())
    print(emp2.fullname())


if __name__ == '__main__':
    main()