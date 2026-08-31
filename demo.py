#!/usr/bin/env python
"""
Demonstration of the Arithmetic Formatter function.
Shows various examples of how the function works.
"""

from arithmetic_arranger import arithmetic_arranger

print("=" * 60)
print("ARITHMETIC FORMATTER - DEMONSTRATION")
print("=" * 60)

# Example 1: Simple addition and subtraction
print("\n1. Basic example with addition and subtraction:")
print("-" * 60)
problems1 = ["3801 - 2", "123 + 49"]
result1 = arithmetic_arranger(problems1)
print("Input:", problems1)
print("\nOutput:")
print(result1)

# Example 2: Multiple problems
print("\n\n2. Multiple problems (4 problems):")
print("-" * 60)
problems2 = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
result2 = arithmetic_arranger(problems2)
print("Input:", problems2)
print("\nOutput:")
print(result2)

# Example 3: Maximum problems with answers
print("\n\n3. Maximum problems (5) with answers displayed:")
print("-" * 60)
problems3 = ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
result3 = arithmetic_arranger(problems3, True)
print("Input:", problems3)
print("Show answers: True")
print("\nOutput:")
print(result3)

# Example 4: Simple addition with answers
print("\n\n4. Simple problems with answers:")
print("-" * 60)
problems4 = ["3 + 855", "988 + 40"]
result4 = arithmetic_arranger(problems4, True)
print("Input:", problems4)
print("Show answers: True")
print("\nOutput:")
print(result4)

# Example 5: Error - too many problems
print("\n\n5. Error example: Too many problems")
print("-" * 60)
problems5 = ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]
result5 = arithmetic_arranger(problems5)
print("Input:", problems5)
print("Result:", result5)

# Example 6: Error - invalid operator
print("\n\n6. Error example: Invalid operator")
print("-" * 60)
problems6 = ["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]
result6 = arithmetic_arranger(problems6)
print("Input:", problems6)
print("Result:", result6)

# Example 7: Error - numbers too long
print("\n\n7. Error example: Numbers too long")
print("-" * 60)
problems7 = ["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]
result7 = arithmetic_arranger(problems7)
print("Input:", problems7)
print("Result:", result7)

# Example 8: Error - non-digit characters
print("\n\n8. Error example: Non-digit characters")
print("-" * 60)
problems8 = ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]
result8 = arithmetic_arranger(problems8)
print("Input:", problems8)
print("Result:", result8)

# Example 9: Negative results
print("\n\n9. Problems with negative results:")
print("-" * 60)
problems9 = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"]
result9 = arithmetic_arranger(problems9, True)
print("Input:", problems9)
print("Show answers: True")
print("\nOutput:")
print(result9)

print("\n" + "=" * 60)
print("END OF DEMONSTRATION")
print("=" * 60)
