def calculator(x,y,op):
    
    if type(x) != int or type(y) != int: return 'unknown value'
    if str(op) not in '+-*/': return 'unknown value'
    if op == '+': return x + y
    if op == '-': return x - y
    if op == '*': return x * y
    if op == '/': return x / y  