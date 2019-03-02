from typing import List, Any

from src.Employee import Employee


class Manager(Employee):

    def __init__(self, first, last, pay, progl = None):
        super().__init__(first, last, pay)
        if progl is not None:
            self.progL = progl
        else:
            self.progL = []

    def fullname(self):
        return super().fullname() + ' ' + str(self.progL)

    def add_prog_l(self, lang):
        return self.progL.append(lang)

    def applay_raise(self, amount=1.04):
        if amount == 1.04:
            self.pay = self.pay * 1.04
        else:
            self.pay = self.pay * amount

    def __str__(self):
        return '{} {} {} {}'.format(self.first, self.last, self.pay, self.progL)
    
    def __add__(self, other):
        if isinstance(other, Manager):
            return Manager(self.first + "---" + other.first, self.last + "---" + other.last, self.pay + other.pay, self.progL + other.progL)
        else:
            return NotImplemented


def main():
    m1 = Manager('Denisu', 'Ferry', 10, ['Python', 'Java', 'C++'])
    m2 = Manager('Sergiu', 'Zeu la Muieri', 100)

    print(m1)
    print(m2)
    m1.applay_raise()
    m2.applay_raise(1.01)
    print(m1.fullname())
    print(m2.fullname())
    m2.add_prog_l('PHP')
    m2.add_prog_l('Lisp')
    print(m2)


if __name__ == '__main__':
    main()

