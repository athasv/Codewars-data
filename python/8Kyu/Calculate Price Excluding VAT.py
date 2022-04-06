def excluding_vat_price(price):
    return round( price / 1.15, 2) if price is not 0 and price is not None and price is not '' else -1