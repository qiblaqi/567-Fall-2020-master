def classify_triangle(a: float, b: float, c: float) -> str:
    if a <= 0 or b <= 0 or c <= 0:
        return "not a triangle"
    if a*a == b*b + c*c or b*b == a*a + c*c or a*a + b*b == c*c:
        return "right"
    if a == b and b == c and a != 0:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isoceles"
    elif a != b and a != c and b != c:
        return "scalene"
    else:
        return "not a triangle"