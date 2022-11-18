import numpy as np

def get_list(matrix):
    with open(f"/home/alex/Escritorio/Computacion-II/celery/{matrix}", "r") as f:
        matrix_a = f.read().splitlines()
        list_num = []
        rows = 0
        columns = 0
        for num in matrix_a:
            rows += 1
            num = num.split(", ")
            for n in num:
                if rows == 1:
                    columns += 1
                list_num.append(int(n))
    return list_num, rows, columns