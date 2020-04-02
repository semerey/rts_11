import matplotlib.pyplot as plt
import random
import math
import time

def func_time(f):
    def func(*args):
        start_time = time.time()
        a = f(*args)
        print(f"({f.__name__})час:", (time.time() - start_time))
        return a
    return func

n = 12
omega = 2700
N = 64
range_min = 0
range_max = 1

#@func_time
def signal_func(n, omega, N, min_v=0, max_v=1):
    A = [min_v + (max_v - min_v) * random.random() for _ in range(n)]
    phi = [min_v + (max_v - min_v) * random.random() for _ in range(n)]

    def f(t):
        x = 0
        for i in range(n):
            x += A[i]*math.sin(omega/n*t*i + phi[i])
        return x
    return f

@func_time
def M(x):
    return sum(x)/len(x)

@func_time
def D(x, m=None):
    if m is None:
        m = M(x)
    return sum([(i - m) ** 2 for i in x]) / (len(x) - 1)

s_gen = signal_func(n, omega, N, range_min, range_max)
s = [s_gen(i) for i in range(N)]
m = M(s)
D = D(s, m)
print("m:", m)
print("D:", D)

fig, ax = plt.subplots()
ax.plot(range(N), s)
plt.show()
fig.savefig('Графік')