def find_slope(points):
    r1 = points[3]-points[1]
    r2 = points[2]-points[0]
    return str(int(r1/r2)) if r2 !=0 else "undefined"