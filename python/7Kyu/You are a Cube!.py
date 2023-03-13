def you_are_a_cube(cube):
    return True if round(abs(cube) ** (1 / 3)) ** 3 == abs(cube) else False