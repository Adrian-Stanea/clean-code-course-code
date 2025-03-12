from pydantic.dataclasses import dataclass


@dataclass
class Point2D:
    X: float = 0.0
    Y: float = 0.0


class Rectangle:
    def __init__(self, origin: Point2D, width: float, height: float):
        self.origin = origin
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def print_end_points(self):
        """
        Prints the coordinates of the rectangle's end points.
        """
        bottom_left, bottom_right, top_right = self.compute_edges()


        print(f"Origin: {self.origin}")
        print(f"Top Right: {top_right}")
        print(f"Bottom Left: {bottom_left}")
        print(f"Bottom Right: {bottom_right}")

    def compute_edges(self):
        offsetX = self.origin.X + self.width
        offsetY = self.origin.Y + self.height

        bottom_left = Point2D(self.origin.X, offsetY)
        bottom_right = Point2D(offsetX, offsetY)
        top_right = Point2D(offsetX, self.origin.Y)
        return bottom_left, bottom_right, top_right

    def display(self):
        print(f"Origin: {self.origin}")
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")


def build_rectangle() -> Rectangle:
    point = Point2D(X=50, Y=100)
    rectangle = Rectangle(origin=point, width=90, height=10)
    return rectangle


rectangle = build_rectangle()
rectangle.display()

print(f"Rectangle Area: {rectangle.get_area()}")
rectangle.print_end_points()
