class Animal:
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name, animal_type='omnivore'):
        super().__init__(name)
        self.animal_type = animal_type

    def eat(self):
        food = ''
        if self.animal_type == 'omnivore':
            food = 'plants and meat'
        elif self.animal_type == 'herbivore':
            food = 'plants'
        elif self.animal_type == 'carnivore':
            food = 'meat'

        print(f'{self.name} is eating {food}.')

    def run(self):
        print(f'{self.name} is running.')


class Bird(Animal):
    def __init__(self, name, eggs=0):
        super().__init__(name)
        self.eggs = eggs

    def lay_eggs(self):
        print(f'{self.name} is laying {self.eggs} eggs.')

    def fly(self):
        print(f'{self.name} is flying.')


class Fish(Animal):
    def __init__(self, name, animal_type='omnivore'):
        super().__init__(name)
        self.animal_type = animal_type

    def swim(self):
        print(f'{self.name} is swimming.')

    def eat(self):
        food = ''
        if self.animal_type == 'omnivore':
            food = 'underwater plants and meat'
        elif self.animal_type == 'herbivore':
            food = 'underwater plants'
        elif self.animal_type == 'carnivore':
            food = 'meat'

        print(f'{self.name} is eating {food}.')


def main():
    mammal = Mammal('Tiger', 'carnivore')
    mammal.eat()
    mammal.run()
    print()

    bird = Bird('Eagle', 2)
    bird.lay_eggs()
    bird.fly()
    print()

    fish = Fish('Shark', 'carnivore')
    fish.eat()
    fish.swim()


if __name__ == '__main__':
    main()
