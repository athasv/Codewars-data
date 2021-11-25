def rental_car_cost(d):
    total = d * 40
    return total - 50 if d >= 7 else (total - 20 if d >= 3 else total)