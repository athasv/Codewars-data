def enough(cap, on, wait):
    return 0 if cap - on > wait else wait -(cap - on)
    
print(enough(10,5,5))
print(enough(100,60,50))