# QUESTION c : RUNGE - KUTTA FOURTH

def runge_kutta_fourth_order(f, x0, y0, h, num_steps):
    x = x0
    y = y0

    for _ in range(num_steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x = x + h

    return x, y

def f(x, y):
    return 2 * x * y / (1 + x**2)

x0 = 0
y0 = 0
h = 0.1

xVals = [0.1, 0.2, 0.3]
yVals = []

for i in xVals:
    num_steps = int((i - x0) / h)
    xf, yf = runge_kutta_fourth_order(f, x0, y0, h, num_steps)
    yVals.append(yf)

x1, x2, x3 = 0.1, 0.2, 0.3
y1, y2, y3 = yVals[0], yVals[1], yVals[2]

x4 = 0.4

# Adams Predictor formula
yp4 = y3 + h * (55 * f(x3, y3) - 59 * f(x2, y2) + 37 * f(x1, y1) - 9 * f(x0, y0)) / 24
fp4 = f(x4, yp4)
print('Adams Predictor formula')
print('y predicted Value = ', yp4)
print('f(y predicted)  = ', fp4)

# Adams Corrector formula
yc4 = y3 + h * (f(x1, y1) - 5 * f(x2, y2) + 19 * f(x3, y3) + 9 * fp4) / 24
f4 = f(x4, yc4)
print('\nAdams Corrector formula')
print('y Corrected Value = ', yc4)
print('f(y Corrected) = ', f4)

yc4 = y3 + h * (f(x1, y1) - 5 * f(x2, y2) + 19 * f(x3, y3) + 9 * f4) / 24
print('\nRefined y = ', yc4)

print("-----------------------------")

# Milne Predictor formula
yp4 = y0 + 4 * h * (2 * f(x1, y1) - f(x2, y2) + 2 * f(x3, y3)) / 3
fp4 = f(x4, yp4)
print("Milne’s predictor-corrector method")
print('y predicted Value = ', yp4)
print('f(y predicted)  = ', fp4)

# Simpson Corrector formula
yc4 = y2 + h * (f(x2, y2) + 4 * f(x3, y3) + fp4) / 3
f4 = f(x4, yc4)
print('y Corrected Value = ', yc4)
print('f(y Corrected) = ', f4)

yc4 = y2 + h * (f(x2, y2) + 4 * f(x3, y3) + f4) / 3
print('\nRefined y = ', yc4)

print("-----------------------------")
