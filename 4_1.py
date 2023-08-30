"""Напишите функцию для транспонирования матрицы"""

def trans_matrix():
    matrix = [[1, 2], [4, 7], [9, 3]]
    mat_zip = zip(*matrix)
    transp_matrix = [list(row) for row in mat_zip]
    print(transp_matrix)

trans_matrix()