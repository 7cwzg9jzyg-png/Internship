# Time Calculator

A Python function that calculates new times by adding durations to start times in 12-hour format, with optional day-of-week tracking.

## Overview

The `add_time` function adds a duration to a start time in 12-hour clock format (AM/PM) and returns the result. It can optionally track the day of the week and will indicate when the result falls on the next day or multiple days later.

## Features

- **12-Hour Format Support**: Works with AM/PM time format
- **Duration Addition**: Adds hours and minutes to a start time
- **Day Tracking**: Optionally displays the day of the week
- **Multi-Day Support**: Indicates when results are on the next day or multiple days later
- **Case-Insensitive Days**: Day of week input is case-insensitive
- **No External Libraries**: Pure Python implementation

## Function Signature

```python
def add_time(start, duration, day=None):
    """
    Add a duration to a start time in 12-hour format.
    
    Args:
        start (str): Start time in 12-hour format (e.g., '3:30 PM')
        duration (str): Duration in HH:MM format (e.g., '2:12')
        day (str, optional): Starting day of the week (e.g., 'Monday')
    
    Returns:
        str: The new time with optional day of week and days later information
    """
```

## Usage Examples

### Basic Time Addition
```python
from add_time import add_time

# Simple addition
add_time('3:30 PM', '2:12')
# Returns: '5:42 PM'

add_time('11:55 AM', '3:12')
# Returns: '3:07 PM'
```

### Next Day Indication
```python
add_time('10:10 PM', '3:30')
# Returns: '1:40 AM (next day)'

add_time('2:59 AM', '24:00')
# Returns: '2:59 AM (next day)'
```

### Multiple Days Later
```python
add_time('11:59 PM', '24:05')
# Returns: '12:04 AM (2 days later)'

add_time('8:16 PM', '466:02')
# Returns: '6:18 AM (20 days later)'
```

### With Day of Week (Case-Insensitive)
```python
add_time('3:30 PM', '2:12', 'Monday')
# Returns: '5:42 PM, Monday'

add_time('2:59 AM', '24:00', 'saturDay')
# Returns: '2:59 AM, Sunday (next day)'

add_time('11:59 PM', '24:05', 'Wednesday')
# Returns: '12:04 AM, Friday (2 days later)'

add_time('8:16 PM', '466:02', 'tuesday')
# Returns: '6:18 AM, Monday (20 days later)'
```

## Format Specifications

- **Start Time**: 12-hour format with AM/PM (e.g., '3:30 PM', '12:03 AM')
- **Duration**: HH:MM format where hours can be any whole number, minutes 0-59
- **Day of Week**: Optional, case-insensitive (Monday, MONDAY, mOnDaY all work)

### Output Format Rules

1. **Same Day**: `'HH:MM AM/PM'` or `'HH:MM AM/PM, DayName'`
2. **Next Day**: `'HH:MM AM/PM (next day)'` or `'HH:MM AM/PM, DayName (next day)'`
3. **Multiple Days**: `'HH:MM AM/PM (n days later)'` or `'HH:MM AM/PM, DayName (n days later)'`

## Testing

Run the test suite:
```bash
python test_add_time.py
```

All 15 tests should pass ✓

## Demo

View example usage:
```bash
python demo_add_time.py
```

## File Structure

- `add_time.py` - Main implementation
- `test_add_time.py` - Test cases (15 tests, all passing)
- `demo_add_time.py` - Demonstration with examples

## Requirements

- Python 3.x
- No external libraries required
