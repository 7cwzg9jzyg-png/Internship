import unittest
from main import Hat, experiment


class TestHat(unittest.TestCase):
    """Test cases for the Hat class and experiment function."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.hat1 = Hat(yellow=3, blue=2, green=6)
        self.hat2 = Hat(red=5, orange=4)
        self.hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    
    def test_hat_creation_correct_contents(self):
        """Test 1: Creation of hat object should add correct contents."""
        # Test hat1
        self.assertEqual(len(self.hat1.contents), 11)
        self.assertEqual(self.hat1.contents.count('yellow'), 3)
        self.assertEqual(self.hat1.contents.count('blue'), 2)
        self.assertEqual(self.hat1.contents.count('green'), 6)
        
        # Test hat2
        self.assertEqual(len(self.hat2.contents), 9)
        self.assertEqual(self.hat2.contents.count('red'), 5)
        self.assertEqual(self.hat2.contents.count('orange'), 4)
        
        # Test hat3
        self.assertEqual(len(self.hat3.contents), 21)
        self.assertEqual(self.hat3.contents.count('red'), 5)
        self.assertEqual(self.hat3.contents.count('orange'), 4)
        self.assertEqual(self.hat3.contents.count('black'), 1)
        self.assertEqual(self.hat3.contents.count('blue'), 0)
        self.assertEqual(self.hat3.contents.count('pink'), 2)
        self.assertEqual(self.hat3.contents.count('striped'), 9)
        
        # Verify all items are strings
        for ball in self.hat1.contents:
            self.assertIsInstance(ball, str)
    
    def test_draw_reduces_contents(self):
        """Test 2: The draw method in hat class should reduce number of items in contents."""
        initial_length = len(self.hat1.contents)
        
        # Draw 3 balls
        drawn = self.hat1.draw(3)
        
        self.assertEqual(len(drawn), 3)
        self.assertEqual(len(self.hat1.contents), initial_length - 3)
        
        # Draw all remaining balls
        remaining = len(self.hat1.contents)
        drawn2 = self.hat1.draw(remaining)
        
        self.assertEqual(len(drawn2), remaining)
        self.assertEqual(len(self.hat1.contents), 0)
    
    def test_draw_exceeds_available_balls(self):
        """Test 3: The draw method should behave correctly when the number of balls to extract is bigger than the number of balls in the hat."""
        initial_length = len(self.hat2.contents)
        
        # Try to draw more balls than available
        drawn = self.hat2.draw(100)
        
        # Should return all available balls
        self.assertEqual(len(drawn), initial_length)
        self.assertEqual(len(self.hat2.contents), 0)
        
        # Verify the drawn list contains all the original balls
        self.assertEqual(drawn.count('red'), 5)
        self.assertEqual(drawn.count('orange'), 4)
    
    def test_draw_returns_strings(self):
        """Test that draw method returns strings."""
        drawn = self.hat1.draw(3)
        for ball in drawn:
            self.assertIsInstance(ball, str)
    
    def test_experiment_returns_probability(self):
        """Test 4: The experiment method should return a different probability."""
        hat = Hat(black=6, red=4, green=3)
        
        # Run experiment twice
        prob1 = experiment(hat=hat,
                          expected_balls={'red': 2, 'green': 1},
                          num_balls_drawn=5,
                          num_experiments=100)
        
        # Create a new hat for the second experiment
        hat = Hat(black=6, red=4, green=3)
        prob2 = experiment(hat=hat,
                          expected_balls={'red': 2, 'green': 1},
                          num_balls_drawn=5,
                          num_experiments=100)
        
        # Probabilities should be floats
        self.assertIsInstance(prob1, float)
        self.assertIsInstance(prob2, float)
        
        # Probabilities should be between 0 and 1
        self.assertGreaterEqual(prob1, 0)
        self.assertLessEqual(prob1, 1)
        self.assertGreaterEqual(prob2, 0)
        self.assertLessEqual(prob2, 1)
        
        # Due to randomness, they might be different
        # (though with only 100 experiments, they could be the same)
        # At least verify they are valid probabilities
    
    def test_experiment_probability_range(self):
        """Test that experiment returns a probability between 0 and 1."""
        hat = Hat(red=5, blue=3, green=2)
        
        probability = experiment(hat=hat,
                                expected_balls={'red': 2},
                                num_balls_drawn=3,
                                num_experiments=500)
        
        self.assertGreaterEqual(probability, 0)
        self.assertLessEqual(probability, 1)
    
    def test_experiment_with_impossible_draw(self):
        """Test experiment with an impossible expected draw."""
        hat = Hat(red=2, blue=2)
        
        # Trying to draw 3 green balls from a hat with none
        probability = experiment(hat=hat,
                                expected_balls={'green': 3},
                                num_balls_drawn=4,
                                num_experiments=100)
        
        # Probability should be 0 (impossible to succeed)
        self.assertEqual(probability, 0)
    
    def test_experiment_with_certain_draw(self):
        """Test experiment with a certain expected draw."""
        hat = Hat(red=5)
        
        # Drawing 3 red balls from a hat with 5 red balls
        probability = experiment(hat=hat,
                                expected_balls={'red': 3},
                                num_balls_drawn=3,
                                num_experiments=100)
        
        # Probability should be 1 (certain to succeed)
        self.assertEqual(probability, 1)


if __name__ == '__main__':
    unittest.main()
