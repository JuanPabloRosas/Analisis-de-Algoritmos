import math
def polinomial():
    res_exp = 0
    res_pol = 0
    base_exp = 100
    base_pol = 1.000001
    n = 1
    while res_pol <= res_exp:
        n = n + 1
        res_pol = math.pow(base_pol, n)
        print("polinomial ",res_pol)
        res_exp = math.pow(base_exp, n)
        print("exponencial ", res_exp)
    print(n)


polinomial()
