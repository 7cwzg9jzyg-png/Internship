# Arithmetic Formatter

A Python function that formats arithmetic problems vertically and side-by-side, making them easier to solve like students do in primary school.

## Overview

The `arithmetic_arranger` function takes a list of arithmetic problems and arranges them vertically with proper formatting. It can optionally display the answers to each problem.

## Features

- **Vertical Formatting**: Displays arithmetic problems in vertical format
- **Side-by-Side Display**: Shows multiple problems next to each other with proper spacing
- **Answer Display**: Optionally shows the result of each calculation
- **Input Validation**: Validates operators, operand length, and digit-only values
- **Error Handling**: Provides meaningful error messages for invalid input

## Function Signature

```python
def arithmetic_arranger(problems, show_answers=False):
    """
    Arranges arithmetic problems vertically and side-by-side.
    
    Args:
        problems: A list of strings containing arithmetic problems (e.g., ["32 + 698", "3801 - 2"])
        show_answers: Optional boolean to display answers (default False)
    
    Returns:
        A formatted string with problems arranged vertically and side-by-side,
        or an error message if problems are invalid
    """
```

## Usage Examples

### Basic Usage (without answers)
```python
from arithmetic_arranger import arithmetic_arranger

result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(result)
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

### With Answers
```python
result = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
print(result)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Validation Rules

The function validates input and returns error messages for invalid problems:

1. **Too many problems**: Maximum 5 problems allowed
   - Error: `"Error: Too many problems."`

2. **Invalid operator**: Only `+` and `-` are accepted
   - Error: `"Error: Operator must be '+' or '-'."`

3. **Non-digit operands**: Numbers must only contain digits
   - Error: `"Error: Numbers must only contain digits."`

4. **Operand length**: Each operand must be 4 digits or fewer
   - Error: `"Error: Numbers cannot be more than four digits."`

## Format Specifications

When problems are valid, the output follows these rules:

- **Right-aligned numbers**: All operands are right-aligned
- **Operator placement**: Operator and space before the second operand
- **Width calculation**: Determined by the longest operand plus 2 characters
- **Problem spacing**: 4 spaces separate each problem
- **Dashes**: A line of dashes equal to the problem width appears below each problem
- **Answer display**: When enabled, answers are right-aligned in the dash line

## Testing

Run the included test file to verify the implementation:

```bash
python test_arithmetic_arranger.py
```

All 10 test cases should pass, covering:
- Basic formatting
- Error conditions
- Answer display
- Edge cases

## File Structure

- `arithmetic_arranger.py` - Main implementation
- `test_arithmetic_arranger.py` - Test cases and validation

## Requirements

- Python 3.x
