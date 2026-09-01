class Rectangle:
    def __init__(self, width, height):
        """Initialize a Rectangle with width and height."""
        self.width = width
        self.height = height
    
    def set_width(self, width):
        """Set the width of the rectangle."""
        self.width = width
    
    def set_height(self, height):
        """Set the height of the rectangle."""
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        """Return the diagonal length of the rectangle."""
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):

        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        picture = ''
        for _ in range(self.height):
            picture += '*' * self.width + '\n'
        return picture
    
    def get_amount_inside(self, shape):

        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit
    
    def __str__(self):
        """Return string representation of the rectangle."""
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    """A class to represent a square shape, inheriting from Rectangle."""
    
    def __init__(self, side):
        """Initialize a Square with a side length."""
        super().__init__(side, side)
        self.side = side
    
    def set_side(self, side):
        """Set the side length of the square."""
        self.side = side
        self.width = side
        self.height = side
    
    def set_width(self, width):
        """Set the width (and height) of the square."""
        self.set_side(width)
    
    def set_height(self, height):
        """Set the height (and width) of the square."""
        self.set_side(height)
    
    def __str__(self):
        """Return string representation of the square."""
        return f'Square(side={self.side})'
