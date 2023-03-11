import numpy as np

from src.distribution import Distribution
from prettytable import PrettyTable


def calc_characteristics(dist_names, sizes, repeat_num, rounding):
    for dist_name in dist_names:
        for size in sizes:
            mean_list, median_list, z_r_list, z_q_list, z_tr_list, e_list, d_list = [], [], [], [], [], [], []
            lists = [mean_list, median_list, z_r_list, z_q_list, z_tr_list]
            for i in range(repeat_num):
                dist = Distribution(dist_name, size)
                dist.set_distribution()
                arr = sorted(dist.random_numbers)
                mean_list.append(np.mean(arr))
                median_list.append(np.mean(arr))
                z_r_list.append(z_r(arr, size))
                z_q_list.append(z_q(arr, size))
                z_tr_list.append(z_tr(arr, size))
            for elem in lists:
                e_list.append(round(np.mean(elem), rounding))
                d_list.append(round(np.std(elem) ** 2, rounding))
            table = PrettyTable()
            table.field_names = [f"{dist_name} n = " + str(size), "Mean", "Median", "Zr", "Zq", "Ztr"]
            e_list.insert(0, 'E(z)')
            d_list.insert(0, 'D(z)')
            table.add_row(e_list)
            table.add_row(d_list)
            print(table)


def z_r(selection, size):
    return (selection[0] + selection[size - 1]) / 2


def z_p(selection, n_p):
    if n_p.is_integer():
        return selection[int(n_p)]
    else:
        return selection[int(n_p) + 1]


def z_q(selection, size):
    return (z_p(selection, size / 4) + z_p(selection, 3 * size / 4)) / 2


def z_tr(selection, size):
    r = int(size / 4)
    amount = 0
    for i in range(r + 1, size - r + 1):
        amount += selection[i]
    return (1 / (size - 2 * r)) * amount
