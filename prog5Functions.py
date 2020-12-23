import math
def integrate(min, max, n):
    ySum = 0
    functionX = float(min)
    deltaX = (float(max) - float(min)) / int(n)
    for x in n:
        if x == 0 or x == n:
            ySum += f(functionX)
        else:
            ySum += 2 * f(functionX)
        functionX += deltaX
    integral = (0.5 * deltaX * ySum)
    return integral

def f(x):
    return math.sin(x) + (x**2)