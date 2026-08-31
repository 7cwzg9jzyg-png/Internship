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
    
    # Days of the week in order
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Parse start time
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))
    
    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Convert start time to 24-hour format
    if period == 'AM':
        if start_hour == 12:
            start_hour = 0
    else:  # PM
        if start_hour != 12:
            start_hour += 12
    
    # Calculate total minutes from start time
    total_minutes = start_hour * 60 + start_minute
    
    # Add duration
    total_minutes += duration_hour * 60 + duration_minute
    
    # Calculate days passed
    days_passed = total_minutes // (24 * 60)
    
    # Get remaining minutes for the day
    remaining_minutes = total_minutes % (24 * 60)
    new_hour = remaining_minutes // 60
    new_minute = remaining_minutes % 60
    
    # Convert back to 12-hour format
    if new_hour == 0:
        display_hour = 12
        new_period = 'AM'
    elif new_hour < 12:
        display_hour = new_hour
        new_period = 'AM'
    elif new_hour == 12:
        display_hour = 12
        new_period = 'PM'
    else:
        display_hour = new_hour - 12
        new_period = 'PM'
    
    # Format the result time
    result = f'{display_hour}:{new_minute:02d} {new_period}'
    
    # Add day of week if provided
    if day:
        # Normalize day to title case for matching
        day_normalized = day.capitalize()
        current_day_index = days_of_week.index(day_normalized)
        new_day_index = (current_day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        result += f', {new_day}'
    
    # Add days passed information
    if days_passed == 1:
        result += ' (next day)'
    elif days_passed > 1:
        result += f' ({days_passed} days later)'
    
    return result
