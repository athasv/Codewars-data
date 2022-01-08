def sum_str(a, b):
    if a != '' and b != "": return str( int(a) + int(b))
    if a != '' and b == '': return a
    if a == '' and b != '': return b
    if a == '' and b == '': return '0'
    