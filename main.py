import math
from typing import NamedTuple
import numpy as np
import matplotlib.pyplot as plt

class Point(NamedTuple):
    d: float
    F: int
    is_y_zero: bool


# demand curve y = c1 * sqrt(d) + c2 * d / (1 - d)
def y(d):
    c1 = 0.0420881544 # value so that d=25M => y=0.02
    c2 = 0.003

    return c1 * math.sqrt(d) + (c2 * d) / (1 - d)

# inflation rate s = y_i * d - b (y_i = c * F / sqrt(dS))
def s(d, F):
    c = 2.6
    S = 120000000
    b = 0.008

    return (c * F / math.sqrt(d * S)) * d - b

def y_p(p: Point):
    if p.is_y_zero:
        return 1 / (1 + s(p.d, p.F)) - 1

    return (1 + y(p.d)) / (1 + s(p.d, p.F)) - 1

def u_dash(point_b: Point, point_a: Point) -> float:
    y_p_before = y_p(point_b)
    y_p_after = y_p(point_a)

    return (1 + y_p_after) / (1 + y_p_before) - 1

def main():
    d_b = 50/120 # 50M / 120M
    d_a = 33.6/120 # 33.6M / 120M
    F_b = 64
    F_a = 32

    u_dash_nonstaker = u_dash(Point(d_b, F_b, True), Point(d_a, F_a, True))
    print(f"u_dash_nonstaker: {u_dash_nonstaker:.6f}")

    u_dash_destaker_1 = u_dash(Point(d_b, F_b, False), Point(40/120, F_a, False))
    u_dash_destaker_2 = u_dash(Point(d_b, F_b, False), Point(35/120, F_a, False))
    print(f"u_dash_destaker_1: {u_dash_destaker_1:.6f}")
    print(f"u_dash_destaker_2: {u_dash_destaker_2:.6f}")

    d_values = np.linspace(d_b, d_a, 1000)
    u_values = []
    valid_d_values = []

    for d in d_values:
        u = u_dash(Point(d_b, F_b, False), Point(d, F_a, False))
        if not np.isnan(u) and not np.isinf(u) and isinstance(u, (int, float)):
            u_values.append(u)
            valid_d_values.append(d)

    plt.figure(figsize=(10, 6))
    plt.plot(valid_d_values, u_values)
    plt.xlabel('d')
    plt.ylabel('u')
    plt.title("u' of stakers")
    plt.grid(True)
    plt.savefig("u_dash.png")


if __name__ == "__main__":
    main()
