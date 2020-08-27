import re


# Sort of built-in function format
def my_format(my_string, *args):
    if re.search('\{\d\}', my_string) is None:
        reg_exp = '\{' + '\}'
        for arg in args:
            my_string = re.sub(reg_exp, arg, my_string, 1)
    else:
        for  i, arg in enumerate(args):
            reg_exp = '\{' + str(i) + '\}'
            my_string = re.sub(reg_exp, arg, my_string)
    return my_string


# my_string1 = 'letters: {1}, {0}, {2}'
# my_string2 = 'letters: {}, {}, {}'
# my_string3 = 'coordinates: {}, {}'
# print(my_format(my_string1, 'a', 'b', 'c'))
# print(my_format(my_string2, 'a', 'b', 'c'))
# print(my_format(my_string3, '37.4N', '18.3W'))
