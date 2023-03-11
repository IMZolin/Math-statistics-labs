from src.lab1 import build_histogram
from src.lab2 import calc_characteristics

if __name__ == "__main__":
    # initial conditions
    names = ["Normal distribution", "Cauchy distribution", "Laplace distribution", "Poisson distribution",
             "Uniform distribution"]
    sizes = [[10, 50, 1000], [10, 100, 1000], [20, 100], [20, 60, 100]]
    # for lab 1
    colors = ["deepskyblue", "limegreen", "tomato", "blueviolet", "orange"]
    # for lab 2
    repeat_num = 1000
    rounding = 6
    # labs
    build_histogram(names, colors, sizes[0])  # lab 1
    calc_characteristics(names, sizes[1], repeat_num, rounding)  # lab 2
