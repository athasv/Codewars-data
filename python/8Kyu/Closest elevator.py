def elevator(left, right, call):
    pass # Code on! :)
    if left == call and right == call: return "right"
    if abs(call - left) >  abs(call -  right): return "right"
    if abs(call - left) <  abs(call -  right): return "left"
    if abs(call - left) == abs(call -  right): return "right"
    