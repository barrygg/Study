class NonValidInput(Exception):
    def __init__(self, text):
        self.txt = text


# Конвертер арабских чисел в римские

def convert_to_roman(number):
    if not isinstance(number, int):
        raise NonValidInput('Wrong type of argument')
    if number < 1 or number > 4999:
        raise NonValidInput('Wrong value')
    dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
            50: 'L', 40: 'CL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    result = ''
    for key in dict:
        quotient, remainder = divmod(number, key)
        result += (dict[key] * quotient)
        number = remainder
    return result







