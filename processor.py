def print_matrix(mx):
    for x in range(mx.size[0]):
        for y in range(mx.size[1]):
            print(mx.array[x][y], end=' ')
        print()
    return


def is_digit(string):
    if '.' in string:
        return False
    else:
        return True


def add_matrices():
    print("Enter size of first matrix: ", end='')
    size_a = [int(x) for x in input().split(' ')]
    matrix_a = Matrix(size_a)
    print("Enter first matrix:")
    matrix_a.matrix_input()
    print("Enter size of second matrix: ", end='')
    size_b = [int(x) for x in input().split(' ')]
    matrix_b = Matrix(size_b)
    print("Enter second matrix:")
    matrix_b.matrix_input()
    if matrix_a.size != matrix_b.size:
        print("The operation cannot be performed.")
    else:
        result_matrix = Matrix(matrix_a.size)
        for x in range(result_matrix.size[0]):
            for y in range(result_matrix.size[1]):
                result_matrix.array[x][y] = matrix_a.array[x][y] + matrix_b.array[x][y]
        print("The result is")
        print_matrix(result_matrix)


def mult_n(mx, mnozh):
    result_mx = Matrix(mx.size)
    for x in range(mx.size[0]):
        for y in range(mx.size[1]):
            result_mx.array[x][y] = int(mx.array[x][y] * mnozh * 100) / 100
    return result_mx


def mult_mxs():
    print("Enter size of first matrix: ", end='')
    size_a = [int(x) for x in input().split(' ')]
    matrix_a = Matrix(size_a)
    print("Enter first matrix:")
    matrix_a.matrix_input()
    print("Enter size of second matrix: ", end='')
    size_b = [int(x) for x in input().split(' ')]
    matrix_b = Matrix(size_b)
    print("Enter second matrix:")
    matrix_b.matrix_input()
    if matrix_a.size[1] != matrix_b.size[0]:
        print("The operation cannot be performed.")
    else:
        result_size =[matrix_a.size[0], matrix_b.size[1]]
        result_matrix = Matrix(result_size)
        for x in range(result_matrix.size[0]):
            for y in range(result_matrix.size[1]):
                result_matrix.array[x][y] = 0
                i = 0
                while i < matrix_a.size[1]:
                    result_matrix.array[x][y] += matrix_a.array[x][i] * matrix_b.array[i][y]
                    i += 1
        print("The result is")
        print_matrix(result_matrix)


def transpose_menu():
    print()
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = input("Your choice: ")
    print("Enter size of matrix: ", end='')
    size_a = [int(x) for x in input().split(' ')]
    matrix_a = Matrix(size_a)
    print("Enter matrix:")
    matrix_a.matrix_input()
    if choice == '1':
        print_matrix(matrix_a.transpose_main())
    elif choice == '2':
        print_matrix(matrix_a.transpose_sec())
    elif choice == '3':
        print_matrix(matrix_a.transpose_vert())
    elif choice == '4':
        print_matrix(matrix_a.transpose_hor())
    else:
        return


def determinant_menu():
    print()
    print("Enter size of matrix: ", end='')
    size = [int(x) for x in input().split(' ')]
    matrix = Matrix(size)
    print("Enter matrix:")
    matrix.matrix_input()
    print("The result is:")
    print(determinant(matrix))


def determinant(mx):
    if mx.size[0] < 2:
        determ = mx.array[0][0]
    elif mx.size[0] < 3:
        determ = mx.array[0][0] * mx.array[1][1] - mx.array[0][1] * mx.array[1][0]
    else:
        determ = 0
        for y in range(mx.size[0]):
            determ += mx.array[0][y] * minor(mx, 0, y) * ((-1) ** y)
    return determ


def minor(mx, i, j):
    minor_size = [mx.size[0] - 1, mx.size[1] - 1]
    new_mx = Matrix(minor_size)
    a = 0
    for x in range(mx.size[0]):
        if x == i:
            pass
        else:
            b = 0
            for y in range(mx.size[0]):
                if y == j:
                    pass
                else:
                    new_mx.array[a][b] = mx.array[x][y]
                    b += 1
            a += 1
    return determinant(new_mx)


def inverse_menu():
    print()
    print("Enter size of matrix: ", end='')
    size = [int(x) for x in input().split(' ')]
    matrix_a = Matrix(size)
    print("Enter matrix:")
    matrix_a.matrix_input()
    if determinant(matrix_a) == 0:
        print("This matrix doesn't have an inverse.")
    else:
        print("The result is:")
        print(inverse(matrix_a))


def inverse(mx):
    determ_mx = determinant(mx)
    mx_1 = Matrix(mx.size)
    for i in range(mx.size[0]):
        for j in range(mx.size[0]):
            mx_1.array[i][j] = minor(mx, i, j) * (-1) ** (i + j)
    mx_1 = mx_1.transpose_main()
    return mult_n(mx_1, (1 / determ_mx))


class Matrix:

    def __init__(self, size):
        self.size = size
        self.array = [[[0] for x in range(self.size[1])] for y in range(self.size[0])]

    def matrix_input(self):
        self.array = [[int(y) if is_digit(y) else float(y) for y in input().split(' ')] for x in range(self.size[0])]

    def __str__(self):
        print_matrix(self)
        return ''

    def transpose_main(self):
        out_mx = Matrix(self.size)
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                out_mx.array[x][y] = self.array[y][x]
        return out_mx

    def transpose_sec(self):
        out_mx = Matrix(self.size)
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                out_mx.array[x][y] = self.array[self.size[0] - y - 1][self.size[1] - x - 1]
        return out_mx

    def transpose_vert(self):
        out_mx = Matrix(self.size)
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                out_mx.array[x][y] = self.array[x][self.size[1] - y -1]
        return out_mx

    def transpose_hor(self):
        out_mx = Matrix(self.size)
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                out_mx.array[x][y] = self.array[self.size[0] - x -1][y]
        return out_mx


while True:
    print()
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    action = input("Your choice: ")
    if action == '1':
        add_matrices()
    elif action == '2':
        print("Enter size of matrix: ", end='')
        size_a = [int(x) for x in input().split(' ')]
        matrix_a = Matrix(size_a)
        print("Enter matrix:")
        matrix_a.matrix_input()
        n = input("Enter constant: ")
        if n.isdigit():
            n = int(n)
        else:
            n = float(n)
        print("The result is")
        print_matrix(mult_n(matrix_a, n))
    elif action == '3':
        mult_mxs()
    elif action == '4':
        transpose_menu()
    elif action == '5':
        determinant_menu()
    elif action == '6':
        inverse_menu()
    elif action == '0':
        exit()
    else:
        pass



