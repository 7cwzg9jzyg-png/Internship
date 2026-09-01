import copy
import random


class Hat:
   
    def __init__(self, **kwargs):

        self.contents = []
        
        # Convert the kwargs to a contents list with one string per ball
        for color, quantity in kwargs.items():
            self.contents.extend([color] * quantity)
    
    def draw(self, num_balls):
        # If num_balls is greater than contents length, return all balls
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents = []
            return drawn
        
        # Draw num_balls randomly without replacement
        drawn = []
        for _ in range(num_balls):
            # Pick a random index from the remaining contents
            random_index = random.randint(0, len(self.contents) - 1)
            # Remove and add to drawn list
            drawn.append(self.contents.pop(random_index))
        
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    successful_experiments = 0
    
    for _ in range(num_experiments):
        # Create a copy of the hat for this experiment
        hat_copy = copy.deepcopy(hat)
        
        # Draw the specified number of balls
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the balls by color
        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1
        
        # Check if the drawn balls meet or exceed the expected requirements
        success = True
        for color, quantity in expected_balls.items():
            if drawn_count.get(color, 0) < quantity:
                success = False
                break
        
        if success:
            successful_experiments += 1
    
    # Calculate and return the probability
    probability = successful_experiments / num_experiments
    return probability
