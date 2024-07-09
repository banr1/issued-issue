import math

def y(d):
    c1 = 0.042
    c2 = 0.003
    return c1 * math.sqrt(d) + (c2 * d) / (1 - d)

def s(d, F):
    c = 2.6
    S = 120000000
    return (c * F / math.sqrt(d * S)) * d - 0.008

def v(d, F):    
    return (1 + y(d)) / (1 + s(d, F))

def main():
    d1 = 5/12
    d2 = 0.275
    F1 = 64
    F2 = 32

    v1 = v(d1, F1)
    print("v1: ", v1)
    v2 = v(d2, F2)
    print("v2: ", v2)
    v_ratio = v2 / v1 - 1
    print("v_ratio: ", v_ratio)

if __name__ == "__main__":
    main()
