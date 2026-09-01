from main import Hat, experiment


# Example from the problem description
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(f"Probability of drawing at least 2 red and 1 green: {probability:.3f}")


# Example from the problem statement (5 blue, 4 red, 2 green)
hat2 = Hat(blue=5, red=4, green=2)
probability2 = experiment(hat=hat2,
                          expected_balls={'red': 1, 'green': 2},
                          num_balls_drawn=4,
                          num_experiments=2000)
print(f"Probability of drawing at least 1 red and 2 green from (5 blue, 4 red, 2 green): {probability2:.3f}")


# Another example
hat3 = Hat(yellow=3, blue=2, green=6)
probability3 = experiment(hat=hat3,
                          expected_balls={'yellow': 2, 'blue': 1},
                          num_balls_drawn=4,
                          num_experiments=2000)
print(f"Probability of drawing at least 2 yellow and 1 blue from (3 yellow, 2 blue, 6 green): {probability3:.3f}")
