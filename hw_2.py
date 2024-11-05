class Figure:
    unit = 'cm'
    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass



class Square(Figure):
    def __init__(self, side_length):

        self._side_length = side_length

    def calculate_area(self):

        return self._side_length ** 2

    def info(self):

        return f"Square side length: {self._side_length}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}."


# 9. Класс Rectangle (прямоугольник), наследуемый от Figure
class Rectangle(Figure):
    def __init__(self, _length, width):

        self.__length = _length
        self.__width = width
    def calculate_area(self):
        # Площадь прямоугольника = длина * ширина
        return self.__length * self.__width

    def info(self):
        # Выводим информацию о прямоугольнике: длина, ширина и площадь
        return f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}."


# 13.
figures = [
    Square(5),
    Square(7),
    Rectangle(5, 8),
    Rectangle(10, 3),
    Rectangle(6, 4)
]

# 14. Выводим информацию о каждом объекте через метод info
for figure in figures:
    print(figure.info())


