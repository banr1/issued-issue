import math

def v(d, F):
    c1 = 0.042
    c2 = 0.003
    c = 2.6
    S = 120000000

    def y(d):
        return c1 * math.sqrt(d) + (c2 * d) / (1 - d)
    
    def s(d):
        return (c * F / math.sqrt(d * S)) * d - 0.008
    
    return 1 + (1 + y(d)) / (1 + s(d))

def main():
    d1 = 5/12
    d2 = 0.275
    F1 = 64
    F2 = 32

    v1 = v(d1, F1)
    print("v1: ", v1)
    v2 = v(d2, F2)
    print("v2: ", v2)
    v_ratio = v1 / v2 - 1
    print("v_ratio: ", v_ratio)



if __name__ == "__main__":
    main()
