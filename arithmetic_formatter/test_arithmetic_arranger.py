from arithmetic_arranger import arithmetic_arranger

# Test cases from the requirements
test_cases = [
    {
        'input': (["3801 - 2", "123 + 49"],),
        'expected': "  3801      123\n-    2    +  49\n------    -----",
        'description': "Test 1"
    },
    {
        'input': (["1 + 2", "1 - 9380"],),
        'expected': "  1         1\n+ 2    - 9380\n---    ------",
        'description': "Test 2"
    },
    {
        'input': (["3 + 855", "3801 - 2", "45 + 43", "123 + 49"],),
        'expected': "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----",
        'description': "Test 3"
    },
    {
        'input': (["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"],),
        'expected': "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------",
        'description': "Test 4"
    },
    {
        'input': (["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"],),
        'expected': "Error: Too many problems.",
        'description': "Test 5 - Too many problems"
    },
    {
        'input': (["3 / 855", "3801 - 2", "45 + 43", "123 + 49"],),
        'expected': "Error: Operator must be '+' or '-'.",
        'description': "Test 6 - Invalid operator"
    },
    {
        'input': (["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"],),
        'expected': "Error: Numbers cannot be more than four digits.",
        'description': "Test 7 - Numbers too long"
    },
    {
        'input': (["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"],),
        'expected': "Error: Numbers must only contain digits.",
        'description': "Test 8 - Non-digit characters"
    },
    {
        'input': (["3 + 855", "988 + 40"], True),
        'expected': "    3      988\n+ 855    +  40\n-----    -----\n  858     1028",
        'description': "Test 9 - With answers"
    },
    {
        'input': (["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True),
        'expected': "   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028",
        'description': "Test 10 - Multiple problems with answers"
    }
]

print("Running tests...\n")
passed = 0
failed = 0

for test in test_cases:
    result = arithmetic_arranger(*test['input'])
    expected = test['expected']
    
    if result == expected:
        print(f"✓ {test['description']} PASSED")
        passed += 1
    else:
        print(f"✗ {test['description']} FAILED")
        print(f"  Expected:\n{repr(expected)}")
        print(f"  Got:\n{repr(result)}")
        print()
        failed += 1

print(f"\n{passed} passed, {failed} failed")
