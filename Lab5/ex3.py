class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def calc_mileage(self):
        pass

    def calc_towing_capacity(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, year, mass):
        super().__init__(make, model, year)
        self.mass = mass

    def calc_mileage(self):
        return (2023 - self.year) * 13500

    def calc_towing_capacity(self):
        return self.mass * 0.5


class Truck(Vehicle):
    def __init__(self, make, model, year, mass):
        super().__init__(make, model, year)
        self.mass = mass

    def calc_mileage(self):
        return (2023 - self.year) * 1000

    def calc_towing_capacity(self):
        return self.mass * 0.8


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mass):
        super().__init__(make, model, year)
        self.mass = mass

    def calc_mileage(self):
        return (2023 - self.year) * 20000

    def calc_towing_capacity(self):
        return self.mass * 0.3


def main():
    car = Car('Mercedes', 'GLK', 2015, 1925)
    print(f'Car mileage: {car.calc_mileage()}')
    print(f'Car towing capacity: {car.calc_towing_capacity()}')

    truck = Truck('Ford', 'F150', 2022, 4500)
    print(f'Truck mileage: {truck.calc_mileage()}')
    print(f'Truck towing capacity: {truck.calc_towing_capacity()}')

    motorcycle = Motorcycle('Honda', 'CBR1000RR', 2018, 200)
    print(f'Motorcycle mileage: {motorcycle.calc_mileage()}')
    print(f'Motorcycle towing capacity: {motorcycle.calc_towing_capacity()}')


if __name__ == '__main__':
    main()
