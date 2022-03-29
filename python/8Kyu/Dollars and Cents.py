def format_money(amount):
    import re
    return re.sub(r'^(\d+\.\d{,2})\d*$',r'\1',"${:.2f}").format(amount)