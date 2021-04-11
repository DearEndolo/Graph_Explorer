from math import sqrt , cos , sin , pi


class Vector2D(object):
    """Class : Vector2D
    Attributes :
        x: a float, use getter and setter getX() and setX(float) .
        y: a float, use getter and setter getY() and setY(float) .

    Constants :
        ZERO(): return a new Vector2D with x = 0 and y = 0 .
        UP(): return a new Vector2D with x = 0 and y = -1 .

    Methods :
        normalise(): normalise the current vector
        rotate(radiant: float): rotate the current vector by an angle (in radiant) counterclockwise
        rotateDegree(degree: float): rotate the current vector by an angle (in degree) counterclockwise
        rotateFromPivot(pivot: Vector2D, radiant: float): rotate from a pivot point, by an angle (in radiant) counterclockwise
        rotateFromPivotDegree(pivot: Vector2D, degree: float): rotate from a pivot point, by an angle (in degree) counterclockwise
        """

    TO_STRING = "\n\tCoordinates\t( {} , {} )\n"
    __PRECISION__ = 100000

    ZERO = lambda: Vector2D(0.0, 0.0)
    UP = lambda: Vector2D(0.0, -1.0)


    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Create a new Vector2D
        :param x: X value if the vector, default is 0
        :param y: Y value if the vector, default is 0
        """
        super().__init__()
        self.__x = x
        self.__y = y
        self.__floor__()


    #   Vector2D Methods - - - - - - - - - - - -
    def normalise(self):
        """
        Normalise the current vector
        """
        length = sqrt(self.getX() * self.getX() + self.getY() * self.getY())
        self.setX(self.getX() / length)
        self.setY(self.getY() / length)
        self.__floor__()


    def rotate(self, value: float):
        """
        rotate the current vector by an angle (in radiant) counterclockwise
        :param value: angle in radiant
        """
        x = cos(value) * (self.getX()) - sin(value) * (self.getY())
        y = sin(value) * (self.getX()) + cos(value) * (self.getY())
        self.setX(x)
        self.setY(y)
        self.__floor__()

    def rotateDegree(self, value: float):
        """
        rotate the current vector by an angle (in degree) counterclockwise
        :param value: angle in degree
        """
        self.rotate(value * pi / 180)


    def rotateFromPivot(self, pivot, value: float):
        """
        rotate from a pivot point, by an angle (in radiant) counterclockwise
        :param pivot: a Vector2D point
        :type pivot Vector2D
        :param value: angle in radiant
        :return:
        """
        assert type(pivot) == Vector2D
        x = cos(value) * (self.getX() - pivot.getX()) - sin(value) * (self.getY() - pivot.getY()) + pivot.getX()
        y = sin(value) * (self.getX() - pivot.getX()) + cos(value) * (self.getY() - pivot.getY()) + pivot.getY()
        self.setX(x)
        self.setY(y)
        self.__floor__()


    def rotateFromPivotDegree(self, pivot, value: float):
        """
        rotate from a pivot point, by an angle (in degree) counterclockwise
        :param pivot: a Vector2D point
        :type pivot Vector2D
        :param value: angle in degree
        :return:
        """
        self.rotateFromPivot(pivot, value * pi / 180)


    @staticmethod
    def distance(a, b) -> float:
        """
        Get the distance between two points
        :param a: A point
        :type a: Vector2D
        :param b: An another point
        :type b: Vector2D
        :return:  The distance between the two points
        """
        res = sqrt((b.getX() - a.getX())**2 + (b.getY() - a.getY())**2)
        return float(int(res * Vector2D.__PRECISION__) / Vector2D.__PRECISION__)

    #   Getter Methods - - - - - - - - - - - -
    def getX(self) -> float:
        return float(self.__x)


    def getY(self) -> float:
        return float(self.__y)


    #   Setter Methods - - - - - - - - - - - -
    def setX(self, x: float) -> None:
        self.__x = float(x)
        self.__floor__()


    def setY(self, y: float) -> None:
        self.__y = float(y)
        self.__floor__()


    #   Python Methods - - - - - - - - - - - -
    def __str__(self) -> str:
        return str(type(self)) + self.TO_STRING.format(self.getX(), self.getY())


    def __add__(self, other):
        if type(other) == list:
            res = self
            for o in other:
                res = res + o
            return res

        elif type(other) == type(self):
            x = self.getX() + other.getX()
            y = self.getY() + other.getY()
            return Vector2D(x, y)

        else:
            raise NameError("")


    def __sub__(self, other):
        if type(other) == list:
            res = self
            for o in other:
                res = res - o
            return res

        elif type(other) == type(self):
            x = self.getX() - other.getX()
            y = self.getY() - other.getY()
            return Vector2D(x, y)

        else:
            raise NameError("")


    def __mul__(self, other):
        if type(other) == list:
            res = self
            for o in other:
                res = res * o
            return res

        elif type(other) == type(self):
            x = self.getX() * other.getX()
            y = self.getY() * other.getY()
            return Vector2D(x, y)

        elif type(other) == int or type(other) == float:
            x = self.getX() * other
            y = self.getY() * other
            return Vector2D(x, y)

        else:
            raise NameError("")


    def __eq__(self, other) -> bool:
        if type(other) == list:
            res = True
            for o in other:
                res = res and self.__eq__(o)
            return res

        elif type(other) == type(self):
            return (other.getX() == self.getX()) and (other.getY() == self.getY())

        else:
            return False


    def __floor__(self):
        self.__x = float(int(self.getX() * self.__PRECISION__) / self.__PRECISION__)
        self.__y = float(int(self.getY() * self.__PRECISION__) / self.__PRECISION__)
        return self
