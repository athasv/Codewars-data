def approx_equals(a, b):
    a = round(a, 5)
    b = round(b, 5)
    return __import__("math").isclose(a, b, rel_tol=0, abs_tol=1e-3)