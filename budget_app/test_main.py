import unittest
from main import Category, create_spend_chart


class TestCategory(unittest.TestCase):
    """Test cases for the Category class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.food = Category("Food")
        self.clothing = Category("Clothing")
        self.entertainment = Category("Entertainment")
    
    def test_deposit(self):
        """Test deposit method creates correct ledger entry."""
        self.food.deposit(1000, "deposit")
        self.assertEqual(len(self.food.ledger), 1)
        self.assertEqual(self.food.ledger[0], {"amount": 1000, "description": "deposit"})
    
    def test_deposit_no_description(self):
        """Test deposit with no description."""
        self.food.deposit(1000)
        self.assertEqual(self.food.ledger[0], {"amount": 1000, "description": ""})
    
    def test_withdraw(self):
        """Test withdraw method."""
        self.food.deposit(1000, "deposit")
        result = self.food.withdraw(10.15, "groceries")
        self.assertTrue(result)
        self.assertEqual(len(self.food.ledger), 2)
        self.assertEqual(self.food.ledger[1], {"amount": -10.15, "description": "groceries"})
    
    def test_withdraw_no_funds(self):
        """Test withdraw when insufficient funds."""
        result = self.food.withdraw(100)
        self.assertFalse(result)
        self.assertEqual(len(self.food.ledger), 0)
    
    def test_get_balance(self):
        """Test balance calculation."""
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        self.assertAlmostEqual(self.food.get_balance(), 854.33, places=2)
    
    def test_transfer(self):
        """Test transfer method."""
        self.food.deposit(1000, "deposit")
        result = self.food.transfer(50, self.clothing)
        self.assertTrue(result)
        self.assertAlmostEqual(self.food.get_balance(), 950, places=2)
        self.assertAlmostEqual(self.clothing.get_balance(), 50, places=2)
    
    def test_transfer_insufficient_funds(self):
        """Test transfer with insufficient funds."""
        result = self.food.transfer(100, self.clothing)
        self.assertFalse(result)
        self.assertEqual(len(self.food.ledger), 0)
        self.assertEqual(len(self.clothing.ledger), 0)
    
    def test_check_funds(self):
        """Test check_funds method."""
        self.food.deposit(100)
        self.assertTrue(self.food.check_funds(50))
        self.assertFalse(self.food.check_funds(150))
    
    def test_str_representation(self):
        """Test string representation of category."""
        self.food.deposit(1000, "initial deposit")
        self.food.withdraw(10.15, "groceries")
        self.food.withdraw(15.89, "restaurant and more food for dessert")
        self.food.transfer(50, self.clothing)
        
        output = str(self.food)
        self.assertIn("*************Food*************", output)
        self.assertIn("initial deposit        1000.00", output)
        self.assertIn("groceries               -10.15", output)
        self.assertIn("restaurant and more foo -15.89", output)
        self.assertIn("Transfer to Clothing    -50.00", output)
        self.assertIn("Total: 923.96", output)


class TestSpendChart(unittest.TestCase):
    """Test cases for the create_spend_chart function."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.food = Category("Food")
        self.clothing = Category("Clothing")
        self.auto = Category("Auto")
    
    def test_spend_chart_title(self):
        """Test that chart has correct title."""
        self.food.deposit(1000)
        self.food.withdraw(50)
        chart = create_spend_chart([self.food])
        self.assertIn("Percentage spent by category", chart)
    
    def test_spend_chart_no_newline_at_end(self):
        """Test that chart doesn't end with newline."""
        self.food.deposit(1000)
        self.food.withdraw(50)
        chart = create_spend_chart([self.food])
        self.assertFalse(chart.endswith("\n"))
    
    def test_spend_chart_percentages(self):
        """Test correct percentage calculation and display."""
        self.food.deposit(1000)
        self.food.withdraw(50)  # 50%
        
        self.clothing.deposit(1000)
        self.clothing.withdraw(25)  # 25%
        
        chart = create_spend_chart([self.food, self.clothing])
        lines = chart.split("\n")
        
        # Check that 50% line has bar for food but not clothing
        fifty_line = [line for line in lines if line.startswith(" 50|")][0]
        self.assertIn("o", fifty_line)
    
    def test_spend_chart_spacing(self):
        """Test that all lines have consistent spacing."""
        self.food.deposit(1000)
        self.food.withdraw(50)
        
        self.clothing.deposit(1000)
        self.clothing.withdraw(25)
        
        chart = create_spend_chart([self.food, self.clothing])
        lines = chart.split("\n")
        
        # All bar lines should have same length (excluding title)
        bar_lines = [line for line in lines[1:] if "|" in line or "-" in line]
        lengths = [len(line) for line in bar_lines]
        
        # First set of lines should all be same length
        self.assertEqual(len(set(lengths[:11])), 1)


if __name__ == '__main__':
    unittest.main()
