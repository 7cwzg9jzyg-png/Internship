# Polygon Area Calculator

This project demonstrates Object-Oriented Programming (OOP) concepts by creating a Rectangle class and a Square class (which inherits from Rectangle).

The Rectangle class represents a rectangular shape with the following attributes and methods:

**Attributes:**
- `width`: The width of the rectangle
- `height`: The height of the rectangle

**Methods:**
- `set_width(width)`: Set the width of the rectangle
- `set_height(height)`: Set the height of the rectangle
- `get_area()`: Returns the area (width × height)
- `get_perimeter()`: Returns the perimeter (2 × width + 2 × height)
- `get_diagonal()`: Returns the diagonal length (√(width² + height²))
- `get_picture()`: Returns a string representation using asterisks (*). Returns 'Too big for picture.' if width or height exceeds 50
- `get_amount_inside(shape)`: Returns how many times another shape can fit inside this rectangle (without rotation)
- `__str__()`: Returns 'Rectangle(width=W, height=H)'

### Square
The Square class is a subclass of Rectangle and represents a square shape.

**Attributes:**
- `side`: The side length of the square (inherited `width` and `height` are equal)

**Methods:**
- All Rectangle methods inherited
- `set_side(side)`: Set the side length of the square (updates both width and height)
- `set_width(width)`: Overridden to set both width and height to the same value
- `set_height(height)`: Overridden to set both width and height to the same value
- `__str__()`: Returns 'Square(side=S)'

## Usage Example

```python
from shape import Rectangle, Square

# Create and use a Rectangle
rect = Rectangle(10, 5)
print(rect.get_area())       # Output: 50
rect.set_height(3)
print(rect.get_perimeter())  # Output: 26
print(rect)                  # Output: Rectangle(width=10, height=3)
print(rect.get_picture())    # Output: A 10×3 grid of asterisks

# Create and use a Square
sq = Square(9)
print(sq.get_area())         # Output: 81
sq.set_side(4)
print(sq.get_diagonal())     # Output: 5.656854249492381
print(sq)                    # Output: Square(side=4)
print(sq.get_picture())      # Output: A 4×4 grid of asterisks

# Compare shapes
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # Output: 8
```

## Files

- `shape.py`: Main implementation file containing Rectangle and Square classes
- `demo.py`: Demonstration of usage examples
- `test_shape.py`: Unit tests for both classes

## Running Tests

Run the test suite with:
```bash
python test_shape.py
```

Or use unittest discovery:
```bash
python -m unittest test_shape
```

## Running the Demo

Run the demo file with:
```bash
python demo.py
```
