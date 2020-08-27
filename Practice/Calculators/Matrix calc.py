# Variety of operations on matrices:
# Addition, multiplication, dot product, finding the determinant, transpose, inversion

def input_matrix(number=''):
    arr = []
    print(f'Enter size of {number} matrix:')
    m, n = (int(x) for x in input().split())
    print(f'Enter {number} matrix:')
    for _ in range(m):
        arr.append(list(map(float, input().split())))
    if len(arr) != m and any(len(row) != n for row in arr):
        print('The operation cannot be performed.')
    else:
        return m, n, arr


def multiply_scalar(m, n, a, c):
    return [[el * c for el in row] for row in a]


def add_matrices(m_a, n_a, a, m_b, n_b, b):
    if m_a != m_b and n_a != n_b:
        return 'The operation cannot be performed.'
    return [[sum(el) for el in zip(row[0], row[1])] for row in zip(a, b)]


def dot_product(m_a, n_a, a, m_b, n_b, b):
    if n_a != m_b:
        print('The operation cannot be performed.')
    return [[sum([a[i][j] * b[j][k] for j in range(n_a)]) for k in range(n_b)] for i in range(m_a)]


def main_diagonal(m, n, a):
    return [row for row in list(zip(*a))]


def side_diagonal(m, n, a):
    return [row for row in list(zip(*a))[::-1]]


def vertical(m, n, a):
    return [row[::-1] for row in a]


def horizontal(m, n, a):
    return [row for row in a[::-1]]


# add-on function: finding minor
def minor(k, l, a):
    return [row[:l] + row[l + 1:] for row in a[:k] + a[k + 1:]]


def determinant(m, n, a):
    if m != n:
        return 'The operation cannot be performed.'
    if m == 1:
        return a[0][0]
    elif m == 2:
        return a[0][0] * a[1][1] - a[1][0] * a[0][1]
    else:
        return sum([a[0][j] * ((-1) ** j) * determinant(m - 1, n - 1, minor(j, a)) for j in range(n)])


def transpose_choice():
    print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
    t_option = input('Your choice:')
    m, n, a = input_matrix()
    if t_option == '1':
        return main_diagonal(m, n, a)
    elif t_option == '2':
        return side_diagonal(m, n, a)
    elif t_option == '3':
        return vertical(m, n, a)
    elif t_option == '4':
        return horizontal(m, n, a)
    else:
        return 'The operation cannot be performed.'


# add-on function: finding adjugate matrix
def adjugate_matrix(m, n, a):
        return [[(-1) ** (i + j) * determinant(minor(i, j, main_diagonal(m, n, a)))
                 for j in range(n)] for i in range(m)]


def inverse_matrix(m, n, a):
    d = determinant(m, n, a)
    try:
        res = adjugate_matrix(m, n, a) * (1 / d)
    except (ValueError, TypeError, ZeroDivisionError) as e:
        return 'The operation cannot be performed.'
    return res


def choice(option):
    if option == '1':
        m_a, n_a, a = input_matrix(number='first')
        m_b, n_b, b = input_matrix(number='second')
        result = add_matrices(m_a, n_a, a, m_b, n_b, b)
    elif option == '2':
        m, n, a = input_matrix()
        c = float(input('Enter constant:'))
        result = multiply_scalar(m, n, a, c)
    elif option == '3':
        m_a, n_a, a = input_matrix(number='first')
        m_b, n_b, b = input_matrix(number='second')
        result = dot_product(m_a, n_a, a, m_b, n_b, b)
    elif option == '4':
        transpose_choice()
    elif option == '5':
        m, n, a = input_matrix()
        result = determinant(m, n, a)
    elif option == '6':
        m, n, a = input_matrix()
        result = inverse_matrix(m, n, a)
    else:
        result = 'The operation cannot be performed.')
    return result


while True:
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    option = input('Your choice:')
    if option == '0':
        break
    else:
        res = choice(option)
        if not isinstance(res, str):
            print('The result is:')
        print(res)

