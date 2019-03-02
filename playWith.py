from src.Employee import Employee
from src.Manager import Manager


def argumente(*arg):
    return arg


def main():

    emp1 = Employee('Denisu', 'Doarme 3 ore', 2000)
    emp2 = Employee('Mircea', 'Random', 1000000)
    man1 = Manager('oFemeie', "random", 10000)

    print(emp1.fullname)
    print(repr(emp2))
    print(repr(emp2 + emp1))
    print(argumente(man1,emp1, emp2))

    emp1.fullname = 'Denis Feier'
    print(emp1.fullname)

if __name__ == '__main__':
    main()
