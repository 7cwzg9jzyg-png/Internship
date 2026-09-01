# Probability Calculator

A Python project to estimate the probability of drawing certain colored balls from a hat through Monte Carlo simulation experiments.

## Overview

This project implements a `Hat` class to simulate drawing balls from a hat without replacement, and an `experiment` function to estimate the probability of drawing a specific combination of colored balls.

## Features

### Hat Class

The `Hat` class represents a container with balls of different colors.

**Constructor:**
```python
hat = Hat(color1=count1, color2=count2, ...)
```

Example:
```python
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

**Attributes:**
- `contents`: A list of strings where each string represents one ball. Example: `['red', 'red', 'blue']`

**Methods:**
- `draw(num_balls)`: Randomly removes and returns the specified number of balls from the hat. If the requested number exceeds available balls, returns all remaining balls.

### Experiment Function

The `experiment` function performs multiple simulations to estimate the probability of drawing specific balls.

**Parameters:**
- `hat`: A Hat object containing balls to draw from
- `expected_balls`: A dictionary specifying the minimum number of each color to draw (e.g., `{'red': 2, 'green': 1}`)
- `num_balls_drawn`: The number of balls to draw in each experiment
- `num_experiments`: The number of experiments to perform

**Returns:**
- A float representing the estimated probability (successful experiments / total experiments)

**Example:**
```python
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(probability)  # Output: approximately 0.356
```

## How It Works

1. The `experiment` function performs the requested number of experiments
2. In each experiment:
   - A deep copy of the hat is created (to avoid modifying the original)
   - The specified number of balls are drawn randomly
   - The drawn balls are checked against the expected requirements
   - If all expected minimums are met, the experiment is counted as successful
3. The probability is calculated as: `successful_experiments / total_experiments`

## Running the Demo

To see examples of the Probability Calculator in action:

```bash
python demo.py
```

## Notes

- The more experiments performed, the more accurate the probability estimate
- Each run will produce slightly different results due to random sampling
- The random seed is not set, so different probability values will be generated on each run
- Balls are drawn without replacement (sampling without replacement)

## Example Problem

**Question:** Given a hat with 5 blue balls, 4 red balls, and 2 green balls, what is the probability of drawing exactly 4 balls that contain at least 1 red ball and 2 green balls?

**Solution:**
```python
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat,
                         expected_balls={'red': 1, 'green': 2},
                         num_balls_drawn=4,
                         num_experiments=10000)
print(probability)  # Approximate probability: ~0.257
```
