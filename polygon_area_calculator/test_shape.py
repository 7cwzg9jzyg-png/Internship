import unittest
from shape import Rectangle, Square


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""
    
    def test_rectangle_string_representation(self):
        """Test that Rectangle(3, 6) has correct string representation."""
        rect = Rectangle(3, 6)
        self.assertEqual(str(rect), 'Rectangle(width=3, height=6)')
    
    def test_rectangle_area(self):
        """Test that Rectangle(3, 6).get_area() returns 18."""
        rect = Rectangle(3, 6)
        self.assertEqual(rect.get_area(), 18)
    
    def test_rectangle_perimeter(self):
        """Test that Rectangle(3, 6).get_perimeter() returns 18."""
        rect = Rectangle(3, 6)
        self.assertEqual(rect.get_perimeter(), 18)
    
    def test_rectangle_diagonal(self):
        """Test that Rectangle(3, 6).get_diagonal() returns correct value."""
        rect = Rectangle(3, 6)
        self.assertAlmostEqual(rect.get_diagonal(), 6.708203932499369)
    
    def test_rectangle_string_after_set(self):
        """Test that Rectangle string changes after setting new values."""
        rect = Rectangle(3, 6)
        original_str = str(rect)
        rect.set_width(5)
        rect.set_height(10)
        new_str = str(rect)
        self.assertNotEqual(original_str, new_str)
        self.assertEqual(new_str, 'Rectangle(width=5, height=10)')
    
    def test_rectangle_picture(self):
        """Test that get_picture() returns correct string."""
        rect = Rectangle(3, 4)
        picture = rect.get_picture()
        expected = '***\n***\n***\n***\n'
        self.assertEqual(picture, expected)
    
    def test_rectangle_picture_too_big(self):
        """Test that get_picture() returns 'Too big for picture.' if too large."""
        rect = Rectangle(51, 10)
        self.assertEqual(rect.get_picture(), 'Too big for picture.')
        
        rect2 = Rectangle(10, 51)
        self.assertEqual(rect2.get_picture(), 'Too big for picture.')
    
    def test_rectangle_amount_inside_square(self):
        """Test Rectangle(15,10).get_amount_inside(Square(5))."""
        rect = Rectangle(15, 10)
        sq = Square(5)
        self.assertEqual(rect.get_amount_inside(sq), 6)
    
    def test_rectangle_amount_inside_rectangle(self):
        """Test Rectangle(4,8).get_amount_inside(Rectangle(3, 6))."""
        rect1 = Rectangle(4, 8)
        rect2 = Rectangle(3, 6)
        self.assertEqual(rect1.get_amount_inside(rect2), 1)
    
    def test_rectangle_amount_inside_none(self):
        """Test Rectangle(2,3).get_amount_inside(Rectangle(3, 6))."""
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(3, 6)
        self.assertEqual(rect1.get_amount_inside(rect2), 0)


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""
    
    def test_square_is_subclass(self):
        """Test that Square is a subclass of Rectangle."""
        self.assertTrue(issubclass(Square, Rectangle))
    
    def test_square_is_distinct_class(self):
        """Test that Square is a distinct class from Rectangle."""
        self.assertNotEqual(Square, Rectangle)
    
    def test_square_is_instance(self):
        """Test that a Square is instance of both Square and Rectangle."""
        sq = Square(5)
        self.assertIsInstance(sq, Square)
        self.assertIsInstance(sq, Rectangle)
    
    def test_square_string_representation(self):
        """Test that Square(5) has correct string representation."""
        sq = Square(5)
        self.assertEqual(str(sq), 'Square(side=5)')
    
    def test_square_area(self):
        """Test that Square(5).get_area() returns 25."""
        sq = Square(5)
        self.assertEqual(sq.get_area(), 25)
    
    def test_square_perimeter(self):
        """Test that Square(5).get_perimeter() returns 20."""
        sq = Square(5)
        self.assertEqual(sq.get_perimeter(), 20)
    
    def test_square_diagonal(self):
        """Test that Square(5).get_diagonal() returns correct value."""
        sq = Square(5)
        self.assertAlmostEqual(sq.get_diagonal(), 7.0710678118654755)
    
    def test_square_string_after_set_side(self):
        """Test that Square string changes after using set_side()."""
        sq = Square(5)
        original_str = str(sq)
        sq.set_side(3)
        new_str = str(sq)
        self.assertNotEqual(original_str, new_str)
        self.assertEqual(new_str, 'Square(side=3)')
    
    def test_square_string_after_set_width(self):
        """Test that Square string changes after using set_width()."""
        sq = Square(5)
        original_str = str(sq)
        sq.set_width(7)
        new_str = str(sq)
        self.assertNotEqual(original_str, new_str)
        self.assertEqual(new_str, 'Square(side=7)')
    
    def test_square_string_after_set_height(self):
        """Test that Square string changes after using set_height()."""
        sq = Square(5)
        original_str = str(sq)
        sq.set_height(4)
        new_str = str(sq)
        self.assertNotEqual(original_str, new_str)
        self.assertEqual(new_str, 'Square(side=4)')
    
    def test_square_picture(self):
        """Test that get_picture() returns correct string for square."""
        sq = Square(3)
        picture = sq.get_picture()
        expected = '***\n***\n***\n'
        self.assertEqual(picture, expected)
    
    def test_square_picture_too_big(self):
        """Test that get_picture() returns 'Too big for picture.' if too large."""
        sq = Square(51)
        self.assertEqual(sq.get_picture(), 'Too big for picture.')


if __name__ == '__main__':
    unittest.main()
