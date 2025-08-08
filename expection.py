def print_diagonal(matrix):
    try:

        n = len(matrix)
        for row in matrix:
            if len(row) != n:
                raise ValueError("Matrix is not square!")

        print("Diagonal elements:")
        for i in range(n):
            print(matrix[i][i], end=" ")

    except ValueError as ve:
        print("ValueError:", ve)

    except IndexError as ie:
        print("IndexError: Matrix access issue -", ie)

    except Exception as e:
        print("An error occurred:", e)

square_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_diagonal(square_matrix)
