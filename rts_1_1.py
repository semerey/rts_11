import matplotlib.pyplot as plt
import random
import math

n = 12
omega = 2700
N = 64
range_min = 0
range_max = 1

def signal(n, omega, N, min_value=0, max_value=1):
    A = [min_value + (max_value - min_value) * random.random() for _ in range(n)]
    phi = [min_value + (max_value - min_value) * random.random() for _ in range(n)]

    def f(t):
        x = 0
        for i in range(n):
            x += A[i]*math.sin(omega/n*t*i + phi[i])
        return x
    return f

def get_m(x):
    return sum(x)/len(x)

def get_D(x, m=None):
    if m is None:
        m = get_m(x)
    return sum([(i - m) ** 2 for i in x]) / (len(x) - 1)

s_gen = signal(n, omega, N, range_min, range_max)
s = [s_gen(i) for i in range(N)]
m = get_m(s)
D = get_D(s, m)
print("m:", m)
print("D:", D)

fig, ax = plt.subplots()
ax.plot(range(N), s)
plt.show()
fig.savefig('Графік')