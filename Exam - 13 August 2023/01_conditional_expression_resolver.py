def conditional_expression_resolver(expression, idx):
    if expression[idx].isdigit():
        return expression[idx]

    if expression[idx] == 't':
       return conditional_expression_resolver(expression, idx + 2)

    cursor = idx + 2
    statements_counter = 0
    while True:
        symbol = expression[cursor]
        if symbol == '?':
            statements_counter += 1
        elif symbol == ':':
            if statements_counter == 0:
                return conditional_expression_resolver(expression, cursor + 1)
            statements_counter -= 1
        cursor += 1
expression =  input().split()


print(conditional_expression_resolver(expression, 0))