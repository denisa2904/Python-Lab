class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, project=None, department=None):
        super().__init__(name, salary)
        self.project = project
        self.department = department

    def work(self):
        print(f'{self.name} is giving tasks to employees working on {self.project} project.')

    def give_raise(self, name):
        print(f'{self.name} is giving raise to {name}.')


class Engineer(Employee):
    def __init__(self, name, salary, manager, project=None):
        super().__init__(name, salary)
        self.project = project
        self.manager = manager

    def work(self):
        print(f'{self.name} is working on {self.project} project.')

    def request_raise(self):
        print(f'{self.name} is requesting raise from {self.manager}.')


class Salesperson(Employee):
    def __init__(self, name, salary, manager=None):
        super().__init__(name, salary)
        self.manager = manager

    def work(self):
        print(f'{self.name} is selling products.')

    def request_raise(self):
        print(f'{self.name} is requesting raise from {self.manager}.')


def main():
    manager = Manager('John', 10000, 'Project X', 'IT')
    manager.work()

    engineer = Engineer('Bob', 5000, manager.name, 'Project X')
    engineer.work()
    engineer.request_raise()
    manager.give_raise(engineer.name)

    salesperson = Salesperson('Alice', 3000, manager.name)
    salesperson.work()
    salesperson.request_raise()


if __name__ == '__main__':
    main()
