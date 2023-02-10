def solution(m1, m2, gm1, gm2, v, t) :
    return (( gm1 * 0.001/m1 + gm2 * 0.001/m2 ) * 0.082 * (t + 273.15) / v) * 1000	