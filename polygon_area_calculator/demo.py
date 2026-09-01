from shape import Rectangle, Square

# Create a rectangle with width 10 and height 5
rect = Rectangle(10, 5)
print(rect.get_area())  # Should print: 50
rect.set_height(3)
print(rect.get_perimeter())  # Should print: 26
print(rect)  # Should print: Rectangle(width=10, height=3)
print(rect.get_picture())  # Should print a 10x3 rectangle of asterisks

# Create a square with side 9
sq = Square(9)
print(sq.get_area())  # Should print: 81
sq.set_side(4)
print(sq.get_diagonal())  # Should print: 5.656854249492381
print(sq)  # Should print: Square(side=4)
print(sq.get_picture())  # Should print a 4x4 square of asterisks

# Test get_amount_inside
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # Should print: 8
