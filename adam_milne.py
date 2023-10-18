# MILNE, ADAM BASHFORTH

def f(x, y):
    return ((1 + x**2) * y**2) / 2

h = 0.1

x0 = 0
y0 = 1

x1 = 0.1
y1 = 1.06

x2 = x0 + h
y2 = 1.12

x3 = x1 + h
y3 = 1.21

x4 = x3 + h  # x4 corresponds to 0.4

# Adams Predictor formula
yp4 = y3 + h * (55 * f(x3, y3) - 59 * f(x2, y2) + 37 * f(x1, y1) - 9 * f(x0, y0)) / 24
x4 = x3 + h
fp4 = f(x4, yp4)
print('Adams Predictor formula')
print('y predicted Value = ', yp4)
print('f(y predicted) = ', fp4)

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
x4 = x3 + h
fp4 = f(x4, yp4)
print("\nMilne’s predictor corrector method")
print('y predicted Value = ', yp4)
print('f(y predicted) = ', fp4)

# Simpson Corrector formula
yc4 = y2 + h * (f(x2, y2) + 4 * f(x3, y3) + fp4) / 3
f4 = f(x4, yc4)
print('\ny Corrected Value = ', yc4)
print('f(y Corrected) = ', f4)

yc4 = y2 + h * (f(x2, y2) + 4 * f(x3, y3) + f4) / 3
print('\nRefined y = ', yc4)
