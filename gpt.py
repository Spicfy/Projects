class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class Rectangle:
    def __init__(self, bottom_left, top_right, color):
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.color = color

    def __str__(self):
        return f"Rectangle: Bottom Left ({self.bottom_left.x}, {self.bottom_left.y}), Top Right ({self.top_right.x}, {self.top_right.y}), Color: {self.color}"

    def __repr__(self):
        return str(self)

    def get_bottom_left(self):
        return self.bottom_left

    def get_top_right(self):
        return self.top_right

    def get_color(self):
        return self.color

    def reset_color(self, new_color):
        self.color = new_color

    def get_perimeter(self):
        length = abs(self.top_right.x - self.bottom_left.x)
        width = abs(self.top_right.y - self.bottom_left.y)
        return 2 * (length + width)

    def get_area(self):
        length = abs(self.top_right.x - self.bottom_left.x)
        width = abs(self.top_right.y - self.bottom_left.y)
        return length * width

    def move(self, dx, dy):
        self.bottom_left.move(dx, dy)
        self.top_right.move(dx, dy)

    def intersects(self, other):
        return not (
            self.top_right.x < other.bottom_left.x
            or self.bottom_left.x > other.top_right.x
            or self.top_right.y < other.bottom_left.y
            or self.bottom_left.y > other.top_right.y
        )

    def contains(self, point):
        return (
            self.bottom_left.x <= point.x <= self.top_right.x
            and self.bottom_left.y <= point.y <= self.top_right.y
        )

# Example usage:
point1 = Point(0, 0)
point2 = Point(2, 2)
rectangle1 = Rectangle(point1, point2, "red")

point3 = Point(1, 1)
point4 = Point(3, 3)
rectangle2 = Rectangle(point3, point4, "blue")

print(rectangle1.get_bottom_left())  # Output: Point: (0, 0)
print(rectangle1.get_top_right())    # Output: Point: (2, 2)
print(rectangle1.get_color())        # Output: red

rectangle1.reset_color("green")
print(rectangle1.get_color())        # Output: green

print(rectangle1.get_perimeter())    # Output: 8
print(rectangle1.get_area())         # Output: 4

rectangle1.move(1, 1)
print(rectangle1.get_bottom_left())  # Output: Point: (1, 1)
print(rectangle1.get_top_right())    # Output: Point: (3, 3)

print(rectangle1.intersects(rectangle2))  # Output: True
print(rectangle1.contains(point1))    