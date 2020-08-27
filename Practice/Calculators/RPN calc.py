# Calculations in Python shell: addition, substraction, division, multiplication, power
# You can assign a value to the variable and use it later (variable's name should contain only letters)
# Postfix form: Reverse Polish Notation
precedence = {'-': 1, '+': 1, '*': 2, '/': 2, '^': 3}


def mul(x, y):
    return x * y


def div(x, y):
    return x // y


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def power(x, y):
    return x ** y


def duplicate(s):
    s = s.replace(' ', '')
    if s.startswith('-'):
        s = s.replace('-', '0-', 1)
    s = s.replace('(-', '(*(0-1)*')
    if '**' in s or '//' or '^^' in s:
        return 0
    chars = {'++': '+', '+-': '-', '-+': '-', '--': '+'}
    for char in chars:
        s = s.replace(char, chars[char])
    if any(s.find(char) > 0 for char in chars):
        s = duplicate(s)
    return s


def assignment(s, d):
    arr = s.split('=')
    if not arr[0].strip().isalpha():
        print('Invalid identifier')
    elif len(arr) > 2:
        print('Invalid assignment')
    elif arr[1].strip().isalpha() and arr[1].strip() not in d:
        print('Unknown variable')
    elif arr[1].strip().isalpha() and arr[1].strip() in d:
        d[arr[0].strip()] = d[arr[1].strip()]
    else:
        try:
            d[arr[0].strip()] = int(arr[1].strip())
        except (TypeError, ValueError):
            print('Invalid assignment')


def variables_to_numbers(d, numbers):
    if isinstance(numbers, int):
        return numbers
    try:
        return [number if number.isdigit() or number in precedence else d[number] for number in numbers]
    except KeyError:
        return 2


def postfix_form(s):
    if s == 0:
        return 0
    postfix = []
    stack = []
    temp =''
    for char in s:
        if char.isdigit() or char.isalpha():
            temp += char
        else:
            if temp.isdigit() or temp.isalpha():
                postfix.append(temp)
                temp = ''
            elif temp:
                return 1
            if char in precedence:
                if not stack or stack[-1] == '(':
                    stack.append(char)
                elif precedence[char] > precedence[stack[-1]]:
                    stack.append(char)
                elif precedence[char] <= precedence[stack[-1]]:
                    while stack:
                        if stack[-1] == '(':
                            break
                        postfix.append(stack.pop())
                    stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack:
                    if stack[-1] == '(':
                        break
                    postfix.append(stack.pop())
                else:
                    return 0
                stack.pop()
    if temp.isdigit() or temp.isalpha():
        postfix.append(temp)
    elif temp:
        return 1
    while stack:
        if stack[-1] == '(':
            return 0
        postfix.append(stack.pop())
    return postfix


def calculating_result(numbers):
    errors = ['Invalid expression', 'Invalid identifier', 'Unknown variable']
    if isinstance(numbers, int):
        return errors[numbers]
    operation_dict = {'-': sub, '+': add, '*': mul, '/': div, '^': power}
    stack = []
    for number in numbers:
        if number not in precedence:
            stack.append(int(number))
        else:
            y = stack.pop()
            x = stack.pop()
            stack.append(operation_dict[number](x, y))
    return stack[-1]


# var_dict = {}
# while True:
#     command = input()
#     if '=' in command:
#         assignment(command, var_dict)
#     elif command == '/exit':
#         print('Bye!')
#         break
#     elif command == '/help':
#         print('The program calculates the sum, sub, mul, div, pow of numbers.')
#         print('You can assign a value to the variable and use it later')
#     elif not command:
#         pass
#     elif command[0] == '/':
#         print('Unknown command')
#     else:
#         pf_expression = variables_to_numbers(var_dict, postfix_form(duplicate(command)))
#         print(calculating_result(pf_expression))

print((-2 ** 4 + 1))

