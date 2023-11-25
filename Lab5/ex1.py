class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__()
        if side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
            raise RuntimeError('Not a triangle')
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


def main():
    circle = Circle(5)
    print(f'Circle area: {circle.area()}')
    print(f'Circle perimeter: {circle.perimeter()}')
    print()

    rectangle = Rectangle(5, 10)
    print(f'Rectangle area: {rectangle.area()}')
    print(f'Rectangle perimeter: {rectangle.perimeter()}')
    print()

    triangle = Triangle(5, 10, 15)
    print(f'Triangle area: {triangle.area()}')
    print(f'Triangle perimeter: {triangle.perimeter()}')
    print()


if __name__ == '__main__':
    main()
