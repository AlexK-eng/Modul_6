from math import pi, sqrt


class Figure:
    sides_count: int = 0
    __sides: int = []
    __color: int = []
    filled: bool = False

    def __init__(self, colors, *sides):

        if not self.__is_valid_color(*colors):
            colors = [0, 0, 0]
        self.__color = list(colors)
        if not self.__is_valid_sides(*sides):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
#        self.__color = [colors]
#        self.__sides = [*sides,]
        self.filled = False


    def get_color(self):
        return self.__color


    def get_sides(self):
        return self.__sides

    def __is_valid_color(self, r, g, b):
        return all(isinstance(color, int) and 0 <= color <= 255 for color in [r, g, b])


    def __is_valid_sides(self, *sides):
        return (len(sides) == self.sides_count and all(isinstance(side, int)
                and side > 0 for side in sides))


    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]


    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)


    def __len__(self):# вычисляем периметр как сумму всех сторон
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1
    __radius = 1

    def __init__(self, colors, *sides):
        super().__init__(colors, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = len(self) / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3


    def __init__(self, colors, *sides):
        super().__init__(color, *sides)


    def get_square(self):
        p = self.__len__()/2 # вычисление полупериметра для формулы Герона
        a, b, c = self.get_sides() # извлечение сторон треугольника
        return sqrt((p * (p - a) * (p - b) * (p - c))) # формула Герона определение площади треугольника


class Cube(Figure):
    sides_count = 12
    __sides = 1

    def __init__(self, colors, *sides):
        if len(sides) != 1:
            sides = [1]
        super().__init__(colors, *sides * 12)


    def set_sides(self, *new_sides):
         if len(new_sides) == 1:
             super().set_sides(*sides * 12)


    def get_volume(self):
        return self.get_sides()[0] ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
