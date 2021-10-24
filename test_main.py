import unittest
from math import pi
from main import Square, Rectangle, Rhombus, Trapezoid, Triangle, Circle
from main import Cube, Parallelepiped, Pyramid, Sphere, Cone, Cylinder


class TestSquare(unittest.TestCase):

    def setUp(self) -> None:
        self.square = Square(3)

    def test_area(self):
        self.assertEqual(self.square.area(), 9)

    def test_diagonal(self):
        self.assertEqual(Square.diagonal(3), 3 * (2 ** (1 / 2)))


class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.rectangle = Rectangle(3, 4)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 12)

    def test_diagonal(self):
        self.assertEqual(Rectangle.diagonal(3, 4), 5)


class TestRhombus(unittest.TestCase):

    def setUp(self) -> None:
        self.rhombus = Rhombus(4, 3)

    def test_area(self):
        self.assertEqual(self.rhombus.area(), 12)


class TestTrapezoid(unittest.TestCase):

    def setUp(self) -> None:
        self.trapezoid = Trapezoid(2, 4, 5)

    def test_area(self):
        self.assertEqual(self.trapezoid.area(), 15)

    def test_middle_line(self):
        self.assertEqual(Trapezoid.middle_line(2, 4), 3)


class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.triangle = Triangle(3, 4, 5)

    def test_area(self):
        self.assertEqual(self.triangle.area(), 6)

    def test_middle_line(self):
        self.assertEqual(Triangle.middle_line(2, 3, 4), (1, 1.5, 2))


class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.circle = Circle(3)

    def test_area(self):
        self.assertEqual(self.circle.area(), 9 * pi)

    def test_circumference(self):
        self.assertEqual(Circle.circumference(3), 6 * pi)


class TestCube(unittest.TestCase):

    def setUp(self) -> None:
        self.cube = Cube(3)

    def test_area(self):
        self.assertEqual(self.cube.area(), 54)

    def test_volume(self):
        self.assertEqual(self.cube.volume(), 27)


class TestParallelepiped(unittest.TestCase):

    def setUp(self) -> None:
        self.parallelepiped = Parallelepiped(3, 4, 5)

    def test_area(self):
        self.assertEqual(self.parallelepiped.area(), 94)

    def test_volume(self):
        self.assertEqual(self.parallelepiped.volume(), 60)

    def test_diagonal(self):
        self.assertEqual(Parallelepiped.p_diagonal(3, 4, 5), 50 ** (1 / 2))


class TestPyramid(unittest.TestCase):

    def setUp(self) -> None:
        self.pyramid = Pyramid(3, 4, 5)

    def test_area(self):
        self.assertEqual(self.pyramid.area(), 3 * (109 ** (1 / 2)) + 9)

    def test_volume(self):
        self.assertEqual(self.pyramid.volume(), 15)


class TestSphere(unittest.TestCase):

    def setUp(self) -> None:
        self.sphere = Sphere(3)

    def test_area(self):
        self.assertEqual(self.sphere.area(), 36 * pi)

    def test_volume(self):
        self.assertEqual(self.sphere.volume(), 36 * pi)


class TestCone(unittest.TestCase):

    def setUp(self) -> None:
        self.cone = Cone(3, 4)

    def test_area(self):
        self.assertEqual(self.cone.area(), 24 * pi)

    def test_volume(self):
        self.assertEqual(self.cone.volume(), 12 * pi)


class TestCylinder(unittest.TestCase):

    def setUp(self) -> None:
        self.cylinder = Cylinder(3, 4)

    def test_area(self):
        self.assertEqual(self.cylinder.area(), 42 * pi)

    def test_volume(self):
        self.assertEqual(self.cylinder.volume(), 36 * pi)
