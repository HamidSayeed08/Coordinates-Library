import math

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        """How the object is going to look when printed"""
        return "({},{})".format(self.x,self.y)

    def distance_to(self,other):
        """The distance between self and other point"""
        return math.sqrt((self.x-other.x)**2  + (self.y-other.y)**2)

    def midpoint(self,other):
        """Calculates the midpoint of self and other"""
        mid_x = (self.x + other.x)/2
        mid_y = (self.y + other.y)/2
        return Point(mid_x,mid_y)

    def slope_to(self,other):
        """Calculates the slope of the line passing through self and other"""
        if self.x == other.x:
            return None
        else:
            return (other.y-self.y)/(other.x-self.x)

    def __eq__(self,other):
        """"Checks if two points are equal using '==' operator"""
        if isinstance(other,Point):
            return self.x == other.x and self.y == other.y
        else:
            return False



class Line:

    def __init__(self,a,b,c):
        """
        Initialize a line in the form Ax + By + C = 0
        a: coefficient of x
        b: coefficient of y
        c: constant term
        """
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        """
        Return a formatted string for the line equation
        Example: "2x + 3y - 4 = 0"
        """
        parts = []
        
        if self.a != 0:
            parts.append(f"{self.a}x")
            
        if self.b != 0:
            sign = "+" if self.b>0 and parts else ""
            parts.append(f"{sign}{self.b}y")
            
        if self.c !=0:
            sign = "+" if self.c>0 and parts else ""
            parts.append(f"{sign}{self.c}")

        return " ".join(parts)+ " = 0"

    @classmethod
    def from_points(cls,p1,p2):
        """
        Creates a Line from two Points.
        """

        if not isinstance(p1,Point) or not isinstance(p2,Point):
            raise TypeError("Both arguments must be Point objects")

        if p1 == p2:
            raise ValueError("Two identical points cannot define a line")

        A = p2.y - p1.y
        B = -(p2.x - p1.x)
        C = (p2.x - p1.x)*p1.y - (p2.y - p1.y)*p1.x

        return cls(A,B,C)

    def contains_point(self,p):
        """
        Check if a given Point lies on this line.
        Returns True if point satisfies the line equation, False otherwise.
        """
        if not isinstance(p,Point):
            raise TypeError("Argument must be Point object")

        return abs(self.a * p.x + self.b * p.y + self.c) < 1e-9

    def is_parallel(self,other):
        """
        Check if this line is parallel to another Line object.
        """
        if not isinstance(other,Line):
            raise TypeError("Argument must be Line object")

        return self.a * other.b == other.a * self.b

    def is_perpendicular(self,other):
        """
        Check if this line is perpendicular to another Line object.
        """
        if not isinstance(other,Line):
            raise TypeError("Argument must be Line object")

        return (self.a * other.a) + (self.b * other.b) == 0



class Vector:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f"<{self.x},{self.y}>")

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

        
    @classmethod
    def from_points(cls,p1,p2):
        """Create a vector from two points"""
        if not isinstance(p1,Point) or not isinstance(p2,Point):
            raise TypeError("Arguments should be Point object")

        x = p2.x - p1.x
        y = p2.y - p1.y
        return Vector(x,y)

    def __add__(self,other):
        """Add two vectors component-wise"""
        if not isinstance(other,Vector):
            raise TypeError("Can only add another Vector")

        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __sub__(self,other):
        """Subtract two vectors component-wise"""
        if not isinstance(other,Vector):
            raise TypeError("Can only subtract another Vector")

        x = self.x - other.x
        y = self.y - other.y
        return Vector(x,y)

    def dot_product(self,other):
        """Dot product of two vectors"""
        if not isinstance(other,Vector):
            raise TypeError("Argument must be Vector")

        return (self.x * other.x) + (self.y * other.y)

    def cross_product(self,other):
        """Cross product in 2D (returns a scalar)"""
        if not isinstance(other,Vector):
            raise TypeError("Argument must be Vector")

        return (self.x * other.y) - (self.y * other.x)

    def magnitude(self):
        """Calculates length of the vector"""
        return math.sqrt((self.x**2)+(self.y**2))

    def angle_with(self,other):
        """Calculates the angle between two vectors"""
        if not isinstance(other,Vector):
            raise TypeError("Argument must be Vector")

        if self.magnitude() == 0 or other.magnitude() == 0:
            raise ValueError("Cannot calculate angle with zero vector")


        dot_prod = self.dot_product(other)
        magnitude = self.magnitude() * other.magnitude()
        cos_theta = max(-1, min(1, dot_prod / magnitude))
        return math.degrees(math.acos(cos_theta))

__all__ = ["Point", "Line", "Vector"]
        