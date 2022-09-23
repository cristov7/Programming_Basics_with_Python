from math import pi
type_figure = input()
if type_figure == "square":
    a = float(input())
    S = a ** 2
    print(f"{S:.3f}")
elif type_figure == "rectangle":
    a = float(input())
    b = float(input())
    S = a * b
    print(f"{S:.3f}")
elif type_figure == "circle":
    r = float(input())
    S = pi * r ** 2
    print(f"{S:.3f}")
elif type_figure == "triangle":
    a = float(input())
    h = float(input())
    S = (a * h) / 2
    print(f"{S:.3f}")
