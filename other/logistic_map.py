import matplotlib.pyplot as plt
import sys

if sys.argv[1] == '--help':
    print("logistic_map.py rate initial iterations")
    exit(0)

def lm(r, x):
    f = r*x*(1-x)
    yield f
    yield from lm(r, f)

gen = lm(float(sys.argv[1]), float(sys.argv[2]))
iterations = int(sys.argv[3])

plt.plot(range(iterations), [next(gen) for _ in range(iterations)])
plt.show()

