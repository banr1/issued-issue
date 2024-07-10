import math
from typing import NamedTuple

class Point(NamedTuple):
    d: float
    F: int
    is_y_zero: bool


def y(d):
    c1 = 0.042
    c2 = 0.003

    return c1 * math.sqrt(d) + (c2 * d) / (1 - d)

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
    d_b = 5/12
    d_a = 0.275
    F_b = 64
    F_a = 32

    u_dash_nonstaker = u_dash(Point(d_b, F_b, True), Point(d_a, F_a, True))
    print(f"u_dash_nonstaker: {u_dash_nonstaker}")


if __name__ == "__main__":
    main()
