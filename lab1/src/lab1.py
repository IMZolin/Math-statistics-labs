from matplotlib import pyplot as plt
import numpy as np
from src.distribution import Distribution


def build_histogram(dist_names, colors, sizes):
    labels = ["size", "distribution"]
    line_type = "k--"
    for i, dist_name in enumerate(dist_names):
        for size in sizes:
            dist = Distribution(dist_name, size)
            dist.set_distribution()
            fig, ax = plt.subplots(1, 1)
            ax.hist(dist.random_numbers, density=True, alpha=0.7, histtype='stepfilled', color=colors[i])
            if dist_name == "Poisson distribution":
                x = np.arange(dist.density.ppf(0.01), dist.density.ppf(0.99))
                ax.plot(x, dist.density.pmf(x), line_type)
            else:
                x = np.linspace(dist.density.ppf(0.01), dist.density.ppf(0.99), num=100)
                ax.plot(x, dist.density.pdf(x), line_type)
            ax.set_xlabel(labels[0] + ": " + str(size))
            ax.set_ylabel(labels[1])
            ax.set_title(dist_name)
            plt.grid()
            plt.show()
