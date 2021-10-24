from math import pi
from math import tan
import tkinter as tk
from tkinter.ttk import Combobox
from typing import Tuple, NoReturn, Any, List
import matplotlib.pyplot as plt
import numpy as np


class Shape:
    title: str = 'Фигура'

    def area(self) -> float:
        pass


class Polygon(Shape):
    title: str = 'Многоульник'

    def area(self) -> float:
        pass


class Square(Polygon):
    title: str = 'Квадрат'

    def __init__(self, a: float) -> None:
        self.a = a

    def area(self) -> float:
        return self.a ** 2

    @staticmethod
    def diagonal(a: float) -> float:
        return a * (2 ** (1 / 2))


class Rectangle(Polygon):
    title: str = 'Прямоугольник'

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def area(self) -> float:
        return self.a * self.b

    @staticmethod
    def diagonal(a: float, b: float) -> float:
        return (a ** 2 + b ** 2) ** (1 / 2)


class Rhombus(Polygon):
    title: str = 'Ромб'

    def __init__(self, a: float, h: float) -> None:
        self.a = a
        self.h = h

    def area(self) -> float:
        return self.a * self.h


class Trapezoid(Polygon):
    title: str = 'Трапеция'

    def __init__(self, a: float, b: float, h: float) -> None:
        self.a = a
        self.b = b
        self.h = h

    def area(self) -> float:
        return ((self.a + self.b) / 2) * self.h

    @staticmethod
    def middle_line(a: float, b: float) -> float:
        return (a + b) / 2


class Triangle(Polygon):
    title: str = 'Треугольник'

    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        p: float = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1/2)

    @staticmethod
    def middle_line(a: float, b: float, c: float) -> Tuple[float, float, float]:
        middle_line_a: float = a / 2
        middle_line_b: float = b / 2
        middle_line_c: float = c / 2
        return middle_line_a, middle_line_b, middle_line_c


class Circle(Shape):
    title: str = 'Окружность'

    def __init__(self, r: float) -> None:
        self.r = r

    def area(self) -> float:
        return pi * (self.r ** 2)

    @staticmethod
    def circumference(r: float) -> float:
        return 2 * pi * r


class Cube(Square):
    title: str = 'Куб'

    def area(self) -> float:
        return 6 * (self.a ** 2)

    def volume(self) -> float:
        return self.a ** 3


class Parallelepiped(Rectangle):
    title: str = 'Параллелепипед'

    def __init__(self, a: float, b: float, c: float) -> None:
        super().__init__(a, b)
        self.c = c

    def area(self) -> float:
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

    def volume(self) -> float:
        return self.a * self.b * self.c

    @staticmethod
    def p_diagonal(a: float, b: float, c: float) -> float:
        return (a**2 + b**2 + c**2) ** (1/2)


class Pyramid(Shape):
    title: str = 'Пирамида'

    def __init__(self, a: float, n: float, h: float) -> None:
        self.a = a
        self.n = n
        self.h = h                                                              # высота, опущенная к основанию

    def area(self) -> float:
        L: float = (self.h ** 2 + (self.a / (2 * tan(pi / self.n))) ** 2) ** (1/2)     # апофема
        s_bp: float = ((self.n * self.a) / 2) * L                                      # площадь боковой поверхности
        s_po: float = (self.n * self.a ** 2) / (4 * tan(pi / self.n))                  # площадь поверхности основания
        return s_bp + s_po

    def volume(self) -> float:
        s_po: float = (self.n * self.a ** 2) / (4 * tan(pi / self.n))
        return round(((s_po * self.h) / 3), 4)


class Sphere(Circle):
    title: str = 'Сфера'

    def area(self) -> float:
        return 4 * pi * self.r ** 2

    def volume(self) -> float:
        return (4 * pi * self.r ** 3) / 3


class Cone(Circle):
    title: str = 'Конус'

    def __init__(self, r: float, h: float) -> None:
        super().__init__(r)
        self.h = h

    def area(self) -> float:
        L: float = (self.r ** 2 + self.h ** 2) ** (1/2)
        return pi * self.r * (self.r + L)

    def volume(self) -> float:
        return (pi * (self.r ** 2) * self.h) / 3


class Cylinder(Circle):
    title: str = 'Цилиндр'

    def __init__(self, r: float, h: float) -> None:
        super().__init__(r)
        self.h = h

    def area(self) -> float:
        return 2 * pi * self.r * (self.h + self.r)

    def volume(self) -> float:
        return pi * self.r ** 2 * self.h


def flat_click(event) -> NoReturn:
    combo_volume.set('')

    second_label['text'] = ''
    third_label['text'] = ''

    first_calc_label['text'] = ''
    second_calc_label['text'] = ''
    third_calc_label['text'] = ''

    calculate_btn.pack(side='left', anchor='nw', padx=34)

    second_entry.pack_forget()
    third_entry.pack_forget()
    draw_btn.pack_forget()

    if combo_flat.get() == 'Окружность':
        first_label['text'] = 'Введите радиус r'
        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)

    if combo_flat.get() == 'Квадрат':
        first_label['text'] = 'Введите сторону a'
        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)

    if combo_flat.get() == 'Прямоугольник':
        first_label['text'] = 'Введите сторону a'
        second_label['text'] = 'Введите сторону b'

        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)
        second_entry.pack(side='left', anchor='nw', padx=14, pady=20)

    if combo_flat.get() == 'Треугольник':
        first_label['text'] = 'Введите сторону a'
        second_label['text'] = 'Введите сторону b'
        third_label['text'] = 'Введите сторону c'

        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)
        second_entry.pack(side='left', anchor='nw', padx=14, pady=20)
        third_entry.pack(side='left', anchor='nw', padx=14, pady=20)

    if combo_flat.get() == 'Трапеция':
        first_label['text'] = 'Введите сторону a'
        second_label['text'] = 'Введите сторону b'
        third_label['text'] = 'Введите высоту h'

        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)
        second_entry.pack(side='left', anchor='nw', padx=14, pady=20)
        third_entry.pack(side='left', anchor='nw', padx=20, pady=20)

    if combo_flat.get() == 'Ромб':
        first_label['text'] = 'Введите сторону a'
        second_label['text'] = 'Введите высоту h'

        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)
        second_entry.pack(side='left', anchor='nw', padx=20, pady=20)


def volume_click(event) -> NoReturn:
    combo_flat.set('')

    calculate_btn.pack(side='left', anchor='nw', padx=34)

    second_label['text'] = ''
    third_label['text'] = ''
    first_calc_label['text'] = ''
    second_calc_label['text'] = ''
    third_calc_label['text'] = ''

    second_entry.pack_forget()
    third_entry.pack_forget()
    draw_btn.pack_forget()

    if combo_volume.get() == 'Куб':
        first_label['text'] = 'Введите сторону a'

        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)

    if combo_volume.get() == 'Параллелепипед':
        first_label['text'] = 'Введите сторону a'
        second_label['text'] = 'Введите сторону b'
        third_label['text'] = 'Введите сторону c'

        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)
        second_entry.pack(side='left', anchor='nw', padx=14, pady=20)
        third_entry.pack(side='left', anchor='nw', padx=14, pady=20)

    if combo_volume.get() == 'Пирамида':
        first_label['text'] = 'Введите сторону a'
        second_label['text'] = 'Количество сторон n'
        third_label['text'] = 'Введите высоту h'

        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)
        second_entry.pack(side='left', anchor='nw', padx=0, pady=20)
        third_entry.pack(side='left', anchor='nw', padx=20, pady=20)

    if combo_volume.get() == 'Сфера':
        first_label['text'] = 'Введите радиус r'

        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)

    if combo_volume.get() == 'Конус':
        first_label['text'] = 'Введите радиус r'
        second_label['text'] = 'Введите высоту h'

        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)
        second_entry.pack(side='left', anchor='nw', padx=11, pady=20)

    if combo_volume.get() == 'Цилиндр':
        first_label['text'] = 'Введите радиус r'
        second_label['text'] = 'Введите высоту h'

        first_entry.pack(side='left', anchor='nw', padx=14, pady=20)
        second_entry.pack(side='left', anchor='nw', padx=11, pady=20)


def click() -> NoReturn:
    first_entry_data = first_entry.get()
    second_entry_data = second_entry.get()
    third_entry_data = third_entry.get()
    third_calc_label['text'] = ''
    draw_btn.pack(side='left', anchor='nw', padx=34)

    if combo_flat.get() == 'Окружность':
        r: float = float(first_entry_data)
        circle: Circle = Circle(r)
        first_calc_label['text'] = f'Площадь окружности: {circle.area()}'
        second_calc_label['text'] = f'Длина окружности: {Circle.circumference(r)}'

        plot_circle = plt.Circle((0, 0), r, color='r', fill=False)
        ax: Any = plt.gca()
        ax.cla()
        ax.set_xlim((-20, 20))
        ax.set_ylim((-20, 20))
        ax.add_patch(plot_circle)

    if combo_flat.get() == 'Квадрат':
        a: float = float(first_entry_data)
        square: Square = Square(a)
        first_calc_label['text'] = f'Площадь квадрата: {square.area()}'
        second_calc_label['text'] = f'Диагональ квадрата: {Square.diagonal(a)}'

        plot_square = plt.Rectangle((0, 0), a, a, color='r', fill=False)
        ax: Any = plt.gca()
        ax.cla()
        ax.set_xlim((-20, 20))
        ax.set_ylim((-20, 20))
        ax.add_patch(plot_square)

    if combo_flat.get() == 'Прямоугольник':
        a: float = float(first_entry_data)
        b: float = float(second_entry_data)
        rectangle: Rectangle = Rectangle(a, b)
        first_calc_label['text'] = f'Площадь прямоугольника: {rectangle.area()}'
        second_calc_label['text'] = f'Диагональ прямоугольника: {Rectangle.diagonal(a, b)}'

        plot_rectangle = plt.Rectangle((0, 0), a, b, color='r', fill=False)
        ax: Any = plt.gca()
        ax.cla()
        ax.set_xlim((-20, 20))
        ax.set_ylim((-20, 20))
        ax.add_patch(plot_rectangle)

    if combo_flat.get() == 'Треугольник':
        a: float = float(first_entry_data)
        b: float = float(second_entry_data)
        c: float = float(third_entry_data)
        triangle: Triangle = Triangle(a, b, c)
        first_calc_label['text'] = f'Площадь треугольника: {triangle.area()}'
        second_calc_label['text'] = f'Средние линии: {Triangle.middle_line(a, b, c)}'

        x: float = (a**2 + b**2 - c**2) / (2*a)           # вычисление координат 3 точки
        y: float = (b**2 - x**2)**(1/2)

        points: Tuple[List[float, float], ...] = ([0, 0], [a, 0], [x, y])
        plot_triangle = plt.Polygon(points, color='r', fill=False)
        ax: Any = plt.gca()
        ax.cla()
        ax.set_xlim((-20, 20))
        ax.set_ylim((-20, 20))
        ax.add_patch(plot_triangle)

    if combo_flat.get() == 'Трапеция':
        a: float = float(first_entry_data)
        b: float = float(second_entry_data)
        h: float = float(third_entry_data)
        trapezoid: Trapezoid = Trapezoid(a, b, h)
        first_calc_label['text'] = f'Площадь трапеции: {trapezoid.area()}'
        second_calc_label['text'] = f'Средняя линия: {Trapezoid.middle_line(a, b)}'

        points: Tuple[List[float, float], ...] = ([0, 0], [a, 0], [a/2+b/2, h], [a/2-b/2, h])
        plot_trapezoid = plt.Polygon(points, color='r', fill=False)
        ax: Any = plt.gca()
        ax.cla()
        ax.set_xlim((-20, 20))
        ax.set_ylim((-20, 20))
        ax.add_patch(plot_trapezoid)

    if combo_flat.get() == 'Ромб':
        a: float = float(first_entry_data)
        h: float = float(second_entry_data)
        rhombus: Rhombus = Rhombus(a, h)
        first_calc_label['text'] = f'Площадь ромба: {rhombus.area()}'
        second_calc_label['text'] = ''

        points: Tuple[List[float, float], ...] = ([0, 0], [a, 0], [a + (a**2 - h**2)**(1/2), h],
                                                  [(a**2 - h**2)**(1/2), h])
        plot_rhombus = plt.Polygon(points, color='r', fill=False)
        ax: Any = plt.gca()
        ax.cla()
        ax.set_xlim((-20, 20))
        ax.set_ylim((-20, 20))
        ax.add_patch(plot_rhombus)

    if combo_volume.get() == 'Куб':
        a: int = int(first_entry_data)
        cube: Cube = Cube(a)
        first_calc_label['text'] = f'Площадь куба: {cube.area()}'
        second_calc_label['text'] = f'Объем куба: {cube.volume()}'

        axes: List[int] = [a, a, a]
        data: Any = np.ones(axes, dtype=np.bool)
        fig: Any = plt.figure()
        ax: Any = fig.add_subplot(111, projection='3d')
        ax.voxels(data, facecolors='r')

    if combo_volume.get() == 'Параллелепипед':
        a: int = int(first_entry_data)
        b: int = int(second_entry_data)
        c: int = int(third_entry_data)
        parallelepiped: Parallelepiped = Parallelepiped(a, b, c)
        first_calc_label['text'] = f'Площадь параллелепипеда: {parallelepiped.area()}'
        second_calc_label['text'] = f'Объем параллелепипеда: {parallelepiped.volume()}'
        third_calc_label['text'] = f'Диагональ параллелепипеда {Parallelepiped.p_diagonal(a, b, c)}'

        axes: List[int] = [a, b, c]
        data: Any = np.ones(axes, dtype=np.bool)
        fig: Any = plt.figure()
        ax: Any = fig.add_subplot(111, projection='3d')
        ax.voxels(data, facecolors='r')

    if combo_volume.get() == 'Пирамида':
        a: int = int(first_entry_data)
        n: int = int(second_entry_data)
        h: int = int(third_entry_data)
        pyramid: Pyramid = Pyramid(a, n, h)
        first_calc_label['text'] = f'Площадь пирамиды: {pyramid.area()}'
        second_calc_label['text'] = f'Объем параллелепипеда: {pyramid.volume()}'

        r: float = a / (2 * np.sin(pi/n))
        X: List[float] = []
        Y: List[float] = []
        Z: Any = np.zeros(n + 1)
        Z[n] = h

        for i in range(0, n):
            x: float = r * np.cos((2 * pi * i) / n)
            y: float = r * np.sin((2 * pi * i) / n)
            X.append(x)
            Y.append(y)

        X.append(0)
        Y.append(0)
        fig: Any = plt.figure()
        ax: Any = fig.add_subplot(111, projection='3d')
        ax.plot_trisurf(X, Y, Z, color='r')

    if combo_volume.get() == 'Сфера':
        r: float = float(first_entry_data)
        sphere: Sphere = Sphere(r)
        first_calc_label['text'] = f'Площадь сферы: {sphere.area()}'
        second_calc_label['text'] = f'Объем сферы: {sphere.volume()}'

        u: Any = np.linspace(0, 2 * pi, 100)
        v: Any = np.linspace(0, pi, 100)

        x: float = r * np.outer(np.cos(u), np.sin(v))
        y: float = r * np.outer(np.sin(u), np.sin(v))
        z: float = r * np.outer(np.ones(np.size(u)), np.cos(v))

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, color='r')

    if combo_volume.get() == 'Конус':
        r: float = float(first_entry_data)
        h: float = float(second_entry_data)
        cone: Cone = Cone(r, h)
        first_calc_label['text'] = f'Площадь конуса: {cone.area()}'
        second_calc_label['text'] = f'Объем конуса: {cone.volume()}'

        theta: Any = np.linspace(0, 2 * pi, 90)
        radius: Any = np.linspace(0, r, 50)
        T, R = np.meshgrid(theta, radius)

        x: float = R * np.cos(T)
        y: float = R * np.sin(T)
        z: float = np.sqrt(x ** 2 + y ** 2) * (h/r)

        fig: Any = plt.figure()
        ax: Any = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z)

        ax.invert_zaxis()

    if combo_volume.get() == 'Цилиндр':
        r: float = float(first_entry_data)
        h: float = float(second_entry_data)
        cylinder: Cylinder = Cylinder(r, h)
        first_calc_label['text'] = f'Площадь цилиндра: {cylinder.area()}'
        second_calc_label['text'] = f'Объем цилиндра: {cylinder.volume()}'

        u: Any = np.linspace(0, 2 * pi, 50)
        height: Any = np.linspace(0, h, 20)

        x: float = r * np.outer(np.sin(u), np.ones(np.size(height)))
        y: float = r * np.outer(np.cos(u), np.ones(np.size(height)))
        z: float = np.outer(np.ones(np.size(u)), height)

        fig: Any = plt.figure()
        ax: Any = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('450x550')

first_frame = tk.Frame(window)
second_frame = tk.Frame(window)
third_frame = tk.Frame(window)

h1 = tk.Label(text='Выберите фигуру',
              font=('Arial', 16, 'bold'),
              height=2
              )
h2 = tk.Label(text='Плоские фигуры',
              font=('Arial', 16),
              height=2
              )
h3 = tk.Label(text='Объемные фигуры',
              font=('Arial', 16),
              height=2
              )

h1.pack()
h2.pack(side='top', anchor='nw', padx=34)

combo_flat = Combobox(window, font='Arial')
combo_flat['values'] = (Circle.title, Square.title, Rectangle.title,
                        Triangle.title, Trapezoid.title, Rhombus.title)
combo_flat.bind("<<ComboboxSelected>>", flat_click)
combo_flat.pack(side='top', anchor='nw', padx=34)

h3.pack(side='top', anchor='nw', padx=34)

combo_volume = Combobox(window, font='Arial')
combo_volume['values'] = (Cube.title, Parallelepiped.title, Pyramid.title,
                          Sphere.title, Cone.title, Cylinder.title)
combo_volume.bind("<<ComboboxSelected>>", volume_click)
combo_volume.pack(side='top', anchor='nw', padx=34)

first_label = tk.Label(first_frame,
                       text='',
                       font=('Arial', 12),
                       justify='left'
                       )
first_entry = tk.Entry(first_frame,
                       width='20')

second_label = tk.Label(second_frame,
                        text='',
                        font=('Arial', 12),
                        justify='left'
                        )
second_entry = tk.Entry(second_frame,
                        width='20')

third_label = tk.Label(third_frame,
                       text='',
                       font=('Arial', 12),
                       justify='left'
                       )
third_entry = tk.Entry(third_frame,
                       width='20')

first_calc_label = tk.Label(text='',
                            font=('Arial', 12),
                            justify='left'
                            )
second_calc_label = tk.Label(text='',
                             font=('Arial', 12),
                             justify='left'
                             )
third_calc_label = tk.Label(text='',
                            font=('Arial', 12),
                            justify='left'
                            )

first_label.pack(side='left', anchor='nw', padx=34, pady=20)
second_label.pack(side='left', anchor='nw', padx=34, pady=20)
third_label.pack(side='left', anchor='nw', padx=34, pady=20)

first_frame.pack(side='top', anchor='nw')
second_frame.pack(side='top', anchor='nw')
third_frame.pack(side='top', anchor='nw')

calculate_btn = tk.Button(text='Вычислить', command=lambda: click())
draw_btn = tk.Button(text='Показать фигуру', command=lambda: plt.show())

first_calc_label.pack(side='top', anchor='nw', padx=34)
second_calc_label.pack(side='top', anchor='nw', padx=34)
third_calc_label.pack(side='top', anchor='nw', padx=34)

window.mainloop()
