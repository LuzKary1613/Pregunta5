import numpy as np


X0 = 88
a = 50
c = 2
m = 100


N = 1000


random_numbers = []


X = X0
for _ in range(N):
    X = (a * X + c) % m
    random_numbers.append(X / m)  


C = 10
W = 0.10


observed_frequencies = np.histogram(random_numbers, bins=C, range=(0, 1))[0]


expected_frequency = N / C


chi_squared = sum((observed_frequencies - expected_frequency) ** 2 / expected_frequency)

print(f"Valor calculado de chi-cuadrado (x^2): {chi_squared}")
