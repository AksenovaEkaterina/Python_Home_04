# Вычислить число pi c заданной точностью d 
# Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = int(input ("введите значение d "))
def PiNum(d):
    import math
    pi = float(f"{math.pi}")
    pi = round(pi,d)
    print (pi)
PiNum(d)   


