# This is the start of the shapes file for WK8D3 Tech Pathways SU 24
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    @abstractmethod
    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        Shape.__init__(self, color)
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, color, length, width):
        Shape.__init__(self, color)
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        Shape.__init__(self, color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

# Main program
def main():
    shapes = [
        Circle("Red", 5),
        Rectangle("Blue", 4, 6),
        Triangle("Green", 3, 4, 5)
    ]
    
    results = []
    for shape in shapes:
        result = {
            "Shape": shape.__class__.__name__,
            "Color": shape.get_color(),
            "Area": shape.calculate_area(),
            "Perimeter": shape.calculate_perimeter()
        }
        results.append(result)
    
    return results

if __name__ == "__main__":
    shape_results = main()
    for shape in shape_results:
        print(shape)
