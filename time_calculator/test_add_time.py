from add_time import add_time

# Test cases
test_cases = [
    {
        'input': ('3:30 PM', '2:12'),
        'expected': '5:42 PM',
        'description': 'Test 1'
    },
    {
        'input': ('11:55 AM', '3:12'),
        'expected': '3:07 PM',
        'description': 'Test 2'
    },
    {
        'input': ('10:10 PM', '3:30'),
        'expected': '1:40 AM (next day)',
        'description': 'Test 3 - Next day'
    },
    {
        'input': ('2:59 AM', '24:00'),
        'expected': '2:59 AM (next day)',
        'description': 'Test 4 - 24 hours'
    },
    {
        'input': ('11:59 PM', '24:05'),
        'expected': '12:04 AM (2 days later)',
        'description': 'Test 5 - 2 days later'
    },
    {
        'input': ('8:16 PM', '466:02'),
        'expected': '6:18 AM (20 days later)',
        'description': 'Test 6 - 20 days later'
    },
    {
        'input': ('11:43 AM', '00:20'),
        'expected': '12:03 PM',
        'description': 'Test 7 - Same day'
    },
    {
        'input': ('3:00 PM', '3:10'),
        'expected': '6:10 PM',
        'description': 'Test 8 - Same day'
    },
    {
        'input': ('3:30 PM', '2:12', 'Monday'),
        'expected': '5:42 PM, Monday',
        'description': 'Test 9 - With day'
    },
    {
        'input': ('2:59 AM', '24:00', 'saturDay'),
        'expected': '2:59 AM, Sunday (next day)',
        'description': 'Test 10 - Day changes (next day)'
    },
    {
        'input': ('11:59 PM', '24:05', 'Wednesday'),
        'expected': '12:04 AM, Friday (2 days later)',
        'description': 'Test 11 - Day changes (2 days)'
    },
    {
        'input': ('8:16 PM', '466:02', 'tuesday'),
        'expected': '6:18 AM, Monday (20 days later)',
        'description': 'Test 12 - Day changes (20 days)'
    },
    {
        'input': ('11:30 AM', '2:32', 'Monday'),
        'expected': '2:02 PM, Monday',
        'description': 'Test 13 - With day (no day change)'
    },
    {
        'input': ('11:43 AM', '00:20'),
        'expected': '12:03 PM',
        'description': 'Test 14 - AM to PM transition'
    },
    {
        'input': ('11:43 PM', '24:20', 'tueSday'),
        'expected': '12:03 AM, Thursday (2 days later)',
        'description': 'Test 15 - PM to AM transition'
    },
]

print("Running add_time tests...\n")
passed = 0
failed = 0

for test in test_cases:
    result = add_time(*test['input'])
    expected = test['expected']
    
    if result == expected:
        print(f"✓ {test['description']} PASSED")
        passed += 1
    else:
        print(f"✗ {test['description']} FAILED")
        print(f"  Expected: {repr(expected)}")
        print(f"  Got:      {repr(result)}")
        print()
        failed += 1

print(f"\n{passed} passed, {failed} failed")
