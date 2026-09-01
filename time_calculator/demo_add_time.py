#!/usr/bin/env python

from add_time import add_time

print("=" * 60)
print("ADD TIME - DEMONSTRATION")
print("=" * 60)

# Example 1: Simple time addition
print("\n1. Simple time addition (same day):")
print("-" * 60)
result = add_time('3:30 PM', '2:12')
print(f"add_time('3:30 PM', '2:12')")
print(f"Result: {result}")

# Example 2: Time addition crossing into next day
print("\n2. Time addition crossing into next day:")
print("-" * 60)
result = add_time('10:10 PM', '3:30')
print(f"add_time('10:10 PM', '3:30')")
print(f"Result: {result}")

# Example 3: Adding exactly 24 hours
print("\n3. Adding exactly 24 hours:")
print("-" * 60)
result = add_time('2:59 AM', '24:00')
print(f"add_time('2:59 AM', '24:00')")
print(f"Result: {result}")

# Example 4: Adding time that spans multiple days
print("\n4. Adding time that spans multiple days:")
print("-" * 60)
result = add_time('8:16 PM', '466:02')
print(f"add_time('8:16 PM', '466:02')")
print(f"Result: {result}")

# Example 5: With day of week (same day)
print("\n5. With day of week (same day):")
print("-" * 60)
result = add_time('3:30 PM', '2:12', 'Monday')
print(f"add_time('3:30 PM', '2:12', 'Monday')")
print(f"Result: {result}")

# Example 6: With day of week (next day)
print("\n6. With day of week (next day):")
print("-" * 60)
result = add_time('2:59 AM', '24:00', 'saturDay')
print(f"add_time('2:59 AM', '24:00', 'saturDay')")
print(f"Result: {result}")

# Example 7: With day of week (multiple days)
print("\n7. With day of week (multiple days):")
print("-" * 60)
result = add_time('11:59 PM', '24:05', 'Wednesday')
print(f"add_time('11:59 PM', '24:05', 'Wednesday')")
print(f"Result: {result}")

# Example 8: Large hour addition with day of week
print("\n8. Large hour addition with day of week:")
print("-" * 60)
result = add_time('8:16 PM', '466:02', 'tuesday')
print(f"add_time('8:16 PM', '466:02', 'tuesday')")
print(f"Result: {result}")

# Example 9: AM to PM transition
print("\n9. AM to PM transition:")
print("-" * 60)
result = add_time('11:43 AM', '00:20')
print(f"add_time('11:43 AM', '00:20')")
print(f"Result: {result}")

# Example 10: PM to AM transition with day change
print("\n10. PM to AM transition with day change:")
print("-" * 60)
result = add_time('11:43 PM', '24:20', 'tueSday')
print(f"add_time('11:43 PM', '24:20', 'tueSday')")
print(f"Result: {result}")

# Example 11: 12 AM edge case
print("\n11. 12 AM edge case:")
print("-" * 60)
result = add_time('11:55 AM', '3:12')
print(f"add_time('11:55 AM', '3:12')")
print(f"Result: {result}")

# Example 12: No time added
print("\n12. No time added:")
print("-" * 60)
result = add_time('3:00 PM', '0:00')
print(f"add_time('3:00 PM', '0:00')")
print(f"Result: {result}")

print("\n" + "=" * 60)
print("END OF DEMONSTRATION")
print("=" * 60)
