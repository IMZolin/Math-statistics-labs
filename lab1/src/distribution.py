from scipy import stats as st
import math


class Distribution:
    def __init__(self, name=None, size=0):
        self.a = None
        self.b = None
        self.name = name
        self.size = size
        self.random_numbers = None
        self.density = None

    def __repr__(self):
        return f"{self.name}\nOn interval: [{self.a}, {self.b}]\nSize: {self.size}\nRandom numbers: " \
               f"{self.random_numbers}\nDensity: {self.density}\n\n"

    def set_distribution(self):
        if self.name == "Normal distribution":
            self.random_numbers = st.norm.rvs(size=self.size)
            self.density = st.norm()
        elif self.name == "Cauchy distribution":
            self.random_numbers = st.cauchy.rvs(size=self.size)
            self.density = st.cauchy()
        elif self.name == "Laplace distribution":
            self.random_numbers = st.laplace.rvs(size=self.size)
            self.density = st.laplace(scale=1 / math.sqrt(2), loc=0)
        elif self.name == "Poisson distribution":
            self.random_numbers = st.poisson.rvs(mu=10, size=self.size)
            self.density = st.poisson(10)  # mu = 10
        elif self.name == "Uniform distribution":
            a = -math.sqrt(3)
            step = 2 * math.sqrt(3)
            self.random_numbers = st.uniform.rvs(size=self.size, loc=a, scale=step)
            self.density = st.uniform(loc=a, scale=step)