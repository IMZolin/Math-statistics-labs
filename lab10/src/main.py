from json import load
# from optparse import Values

import numpy as np
from load_data import load_from_csv, load_octave
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt


def plot_interval(data, eps, part, label="Data intervals"):
    data_n = [t for t in range(1, len(data) + 1)]
    data = [[data[i] - eps, data[i] + eps] for i in range(len(data))]
    w = load_from_csv('w.csv')
    y = []
    for i in range(len(data)):
        plt.vlines(data_n[i], data[i][0], data[i][1], colors = "c", lw = 1)
    if part == 2:
        for i in range(len(data)):
            y.append(0.91916 + 6.2333e-06 * data_n[i])
        plt.plot(data_n, y, 'r')
    elif part == 3:
        for i in range(len(data)):
            y.append(9.1921e-01 + 5.6971e-06 * data_n[i])
        plt.plot(data_n, y, 'r')
        for i in range(len(data)):
            plt.vlines(data_n[i], (data[i][0] + data[i][1]) / 2 - w[i] * eps, (data[i][0] + data[i][1]) / 2 + w[i] * eps, colors = "m", lw = 1)

    plt.xlabel('n')
    plt.ylabel('mV')
    plt.title(label)
    plt.savefig(f"../image/data_and_intervals{part}.png")
    # plt.show()


def plot_omega():
    w0 = load_from_csv('w0.csv')
    w = load_from_csv('w.csv')
    data_n = [t for t in range(1, len(w) + 1)]
    plt.plot(data_n, w0, color="r")
    plt.plot(data_n, w, color='c')
    plt.title('Data intervals')
    plt.xlabel('n')
    plt.ylabel('mV')
    plt.savefig(f"../image/omega.png")
    # plt.show()


def plot_inf_set():
    beta0 = [0.91921, 0.91921, 0.9192, 0.91908, 0.91899, 0.91899, 0.91901, 0.91905, 0.91921]
    beta1 = [5.4802e-06, 6.7974e-06, 6.8769e-06, 7.7739e-06, 8.319e-06, 7.9467e-06, 7.45e-06, 6.2938e-06, 5.4802e-06]
    plt.plot(beta0, beta1, 'co--')

    plt.vlines(0.91899, 5.4802e-06, 8.319e-06, colors="r", lw=1)
    plt.vlines(0.91921, 5.4802e-06, 8.319e-06, colors="r", lw=1)
    plt.hlines(5.4802e-06, 0.91899, 0.91921, colors="r", lw=1)
    plt.hlines(8.319e-06, 0.91899, 0.91921, colors="r", lw=1)

    plt.title('Information set')
    plt.xlabel('beta0')
    plt.ylabel('beta1')
    plt.savefig(f"../image/inform_set.png")
    # plt.show()


def plot_hallway(data, eps, part, label = 'Data intervals'):
    data_n = [t for t in range(1, len(data) + 1)]
    data_n2 = [t for t in range(-50, len(data) + 51)]
    data = [[data[i] - eps, data[i] + eps] for i in range(len(data))]

    for i in range(len(data)):
        plt.vlines(data_n[i], data[i][0], data[i][1], colors="c", lw=1)

    y0 = []
    y1 = []
    if part == 1:
        for i in range(len(data)):
            y0.append(9.1899e-01 + 5.4802e-06 * data_n[i])
            y1.append(9.1921e-01 + 8.3357e-06 * data_n[i])
        plt.plot(data_n, y0, "m--")
        plt.plot(data_n, y1, "m--")
    else:
        for i in range(len(data_n2)):
            y0.append(9.1899e-01 + 5.4802e-06 * data_n2[i])
            y1.append(9.1921e-01 + 8.3357e-06 * data_n2[i])
        plt.plot(data_n2, y0, "m--")
        plt.plot(data_n2, y1, "m--")

    plt.xlabel('n')
    plt.ylabel('mV')
    plt.title(label)
    plt.savefig(f"../image/intervals{part}.png")
    plt.show()


def plot_regress_residuals(data, eps, part):
    data_n = [t for t in range(1, len(data) + 1)]
    y0 = []
    y1 = []
    y2 = []
    for i in range(len(data)):
        y0.append(0.91916 + 6.2333e-06 * data_n[i])
        y1.append(9.1921e-01 + 5.6971e-06 * data_n[i])
        y2.append(0)
    if part == 1:
        for i in range(len(data)):
            plt.vlines(data_n[i], data[i] - y0[i] - eps, data[i] - y0[i] + eps, colors="c", lw=1)
    else:
        for i in range(len(data)):
            plt.vlines(data_n[i], data[i] - y1[i] - eps, data[i] - y1[i] + eps, colors="c", lw=1)
    plt.plot(data_n, y2, 'r')
    plt.title('Data intervals')
    plt.xlabel('n')
    plt.ylabel('mV')
    plt.savefig(f"../image/regression_{part}.png")
    # plt.show()


def find_mu(data, interval):
    count = 0
    for i in range(len(data)):
        if ((data[i][1]) > (interval[1])) and ((data[i][0]) < (interval[0])):
            count = count + 1
    return count

def find_all_mu(data, z):
    mu = []
    for i in range(len(z)):
        mu.append(find_mu(data, z[i]))
    return mu


def plot_mu(data, eps):
    data_n = [t for t in range(1, len(data) + 1)]

    y0 = []
    y1 = []
    for i in range(len(data)):
        y0.append(0.91916 + 6.2333e-06 * data_n[i])
        y1.append(9.1921e-01 + 5.6971e-06 * data_n[i])
    regression0 = []
    regression1 = []
    for i in range(len(data)):
        regression0.append([data[i] - y0[i] - eps, data[i] - y0[i] + eps])
        regression1.append([data[i] - y1[i] - eps, data[i] - y1[i] + eps])
    tmp_z0 = []
    tmp_z1 = []

    for i in range(len(data)):
        tmp_z0.append(regression0[i][0])
        tmp_z0.append(regression0[i][1])
        tmp_z1.append(regression1[i][0])
        tmp_z1.append(regression1[i][1])

    tmp_z0.sort()
    tmp_z1.sort()
    z0 = []
    z1 = []
    for i in range(len(tmp_z0) - 1):
        z0.append([tmp_z0[i], tmp_z0[i + 1]])
        z1.append([tmp_z1[i], tmp_z1[i + 1]])

    mu0 = find_all_mu(regression0, z0)
    mu1 = find_all_mu(regression1, z1)
    mV0 = []
    mV1 = []

    for i in range(len(z0)):
        mV0.append((z0[i][0] + z0[i][1]) / 2)
        mV1.append((z1[i][0] + z1[i][1]) / 2)

    plt.plot(mV0, mu0, color="c")
    plt.plot(mV1, mu1, color="blueviolet")
    plt.title('Mu_calculations')
    plt.xlabel('mV')
    plt.ylabel('mu')
    plt.savefig("../image/input_mu.png")
    # plt.figure()
    # plt.show()


if __name__ == "__main__":
    data = load_from_csv("data/Chanel_1_400nm_2mm.csv")

    eps = 1e-4
    # plot_interval(data, eps, 1)
    # plot_interval(data, eps, 2)
    # plot_interval(data, eps, 3)
    # plot_omega()
    # plot_regress_residuals(data, eps, 1)
    # plot_regress_residuals(data, eps, 2)
    plot_mu(data, eps)
    # plot_inf_set()
    # plot_hallway(data, eps, 1)
    # plot_hallway(data, eps, 2)