# CoordinatesLibrary

A lightweight Python library for working with 2D geometry.
It provides intuitive classes for Points, Lines, and Vectors, designed with clean Object-Oriented Programming principles.
This project was created to apply OOP concepts in practice while building a practical and reusable solution.


FEATURES

  Point
  1. Distance between two points
  2. Midpoint calculation
  3. Slope of a line through two points
  4. Equality checks

  Line
  1. Create a line from two points
  2. Check if a point lies on the line
  3. Test parallelism and perpendicularity

  Vector
  1. Create vectors from coordinates or points
  2. Addition & subtraction (component-wise)
  3. Dot product & cross product
  4. Magnitude (length)
  5. Angle between vectors


USAGE

  from coordinates import Point, Line, Vector
  # Points
  p1 = Point(2, 3)
  p2 = Point(4, 7)
  print(p1.distance_to(p2))   # 4.47
  print(p1.midpoint(p2))      # (3.0, 5.0)
  
  # Line
  line = Line.from_points(p1, p2)
  print(line)                 # 4x - 2y - 2 = 0
  print(line.contains_point(Point(3, 5)))  # True
  
  # Vectors
  v1 = Vector(3, 4)
  v2 = Vector(-4, 5)
  print(v1 + v2)              # <-1,9>
  print(v1.dot_product(v2))   # 8
  print(v1.cross_product(v2)) # 31
  print(v1.angle_with(v2))    # 62.74 (degrees)


TECH DETAILS

Written in Python 3.
Fully object-oriented.
Minimal dependencies (only math).

LICENSE: This project is licensed under the MIT License – free to use, modify, and distribute with attribution.


MOTIVATION

I built this project to sharpen my OOP knowledge and turn abstract math concepts into code.
It’s simple, educational, and a foundation you can build upon for more advanced geometry or graphics projects.
