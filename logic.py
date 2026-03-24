def operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")
    elif op == '%':
        if b != 0:
            return a % b
        else:
            raise ValueError("Cannot divide by zero")
    elif op == '^':
        return a ** b
    else:
        raise ValueError("Invalid operator")
    
def evaluate_expression(expression):

    current_number = ""
    operations = []
    i = 0

    while i < len(expression):
        char = expression[i]
        if char.isdigit() or char == ".":
            current_number += char
        else:
            if current_number:
                operations.append(float(current_number))
                current_number = ""
            operations.append(char)
        i += 1

    if current_number:
        operations.append(float(current_number))  

    while len(operations) > 1:
        if '^' in operations:
            index = operations.index('^')
            result = operation(operations[index - 1], operations[index + 1], '^')
            operations[index - 1:index + 2] = [result]
        elif '*' in operations:
            index = operations.index('*')
            result = operation(operations[index - 1], operations[index + 1], '*')
            operations[index - 1:index + 2] = [result]
        elif '/' in operations:
            index = operations.index('/')
            result = operation(operations[index - 1], operations[index + 1], '/')
            operations[index - 1:index + 2] = [result]
        elif '%' in operations:
            index = operations.index('%')
            result = operation(operations[index - 1], operations[index + 1], '%')
            operations[index - 1:index + 2] = [result]
        elif '+' in operations:
            index = operations.index('+')
            result = operation(operations[index - 1], operations[index + 1], '+')
            operations[index - 1:index + 2] = [result]
        elif '-' in operations:
            index = operations.index('-')
            result = operation(operations[index - 1], operations[index + 1], '-')
            operations[index - 1:index + 2] = [result]

    return operations[0] if operations else 0





