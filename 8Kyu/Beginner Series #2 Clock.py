def past(h, m, s):
    if 0 <= h <= 23:
        if 0 <= m <= 59:
            if 0 <= s <= 59:
                return (h * 3600000) + (m * 60000) + (s * 1000)