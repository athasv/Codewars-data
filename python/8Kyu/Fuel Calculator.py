def fuel_price(litres, price_per_litre):
    if litres >= 2  and litres < 4:  return round((litres * price_per_litre) - (litres * 0.5), 2)
    if litres >= 4  and litres < 6:  return round((litres * price_per_litre) - (litres * 0.10), 2)
    if litres >= 6  and litres < 8: return round((litres * price_per_litre) - (litres * 0.15), 2)
    if litres >= 8 and litres < 10: return round((litres * price_per_litre) - (litres * 0.20), 2)
    if litres >= 10 and litres < 12: return round((litres * price_per_litre) - (litres * 0.25), 2)
    if litres >= 12: return round((litres * price_per_litre) - (litres * 0.25), 2)