import math

def roots(a, b, c):
    if a == 0:
        return "( )"
    d = b * b - 4 * a * c
    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
        if r2 > r1:
            r1, r2 = r2, r1
        return f"({r1}, {r2})"
    elif d == 0:
        r = -b / (2 * a)
        return f"({r})"
    else:
        return "( )"

def value_y(a, b, c, x):
    return a * x * x + b * x + c

def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0 and c == 0:
        return f"f(x) = {a} * X^2"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif c == 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    if a == 0 and b == 0:
        return "f'(x) = 0"
    elif a == 0:
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {2 * a} * X"
    else:
        return f"f'(x) = {2 * a} * X + {b}"

print(roots(1, -3, 2))
print(roots(1, -2, 1))
print(roots(1, 2, 3))

print(value_y(1, -3, 2, 0))
print(value_y(1, -3, 2, 1))
print(value_y(1, -3, 2, -1))

print(to_string(2, -3, 1))
print(to_string(2, 0, 5))
print(to_string(0, 4, -1))
print(to_string(0, 0, 5))

print(derivation(2, -3, 1))
print(derivation(2, 0, 5))
print(derivation(0, 4, -1))
print(derivation(0, 0, 5))