def arithmetic_arranger(problems, show_answers=False):
    
    # Validation: Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Parse and validate each problem
    parsed_problems = []
    
    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
        
        if len(parts) != 3:
            return "Error: Invalid format."
        
        operand1, operator, operand2 = parts
        
        # Validate operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Validate that operands contain only digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Validate operand length (max 4 digits)
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate answer if needed
        num1 = int(operand1)
        num2 = int(operand2)
        
        if operator == '+':
            answer = num1 + num2
        else:  # operator == '-'
            answer = num1 - num2
        
        parsed_problems.append({
            'operand1': operand1,
            'operator': operator,
            'operand2': operand2,
            'answer': answer
        })
    
    # Format the output
    lines = ['', '', '']  # Three lines for operands and dashes, and potentially a fourth for answers
    if show_answers:
        lines.append('')  # Fourth line for answers
    
    for i, problem in enumerate(parsed_problems):
        operand1 = problem['operand1']
        operand2 = problem['operand2']
        operator = problem['operator']
        answer = str(problem['answer'])
        
        # Determine the width of the problem
        # Width is the max of: (operand1 length, operand2 length) + 2 for operator and space
        # Also need to accommodate the answer if showing it
        width = max(len(operand1), len(operand2)) + 2
        if show_answers:
            width = max(width, len(answer))
        
        # Format operand1 (right-aligned)
        line1_part = operand1.rjust(width)
        
        # Format operand2 with operator
        # Operator + space, then operand2 right-aligned in the remaining space
        line2_part = operator + ' ' + operand2.rjust(width - 2)
        
        # Format dashes
        line3_part = '-' * width
        
        # Format answer if needed (right-aligned)
        if show_answers:
            line4_part = answer.rjust(width)
        
        # Add to output lines with proper spacing between problems
        if i > 0:
            # Add spacing between problems
            lines[0] += '    ' + line1_part
            lines[1] += '    ' + line2_part
            lines[2] += '    ' + line3_part
            if show_answers:
                lines[3] += '    ' + line4_part
        else:
            lines[0] += line1_part
            lines[1] += line2_part
            lines[2] += line3_part
            if show_answers:
                lines[3] += line4_part
    
    # Join lines with newlines
    if show_answers:
        return '\n'.join(lines)
    else:
        return '\n'.join(lines[:3])
