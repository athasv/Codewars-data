def array_madness(a,b):
    # Ready, get, set, GO!!!
    return sum(i**2 for i in a) > sum(j**3 for j in b)
	
def array_madness(a,b):
    return True if sum(map(lambda x:x**2,a)) > sum(map(lambda x:x**3,b)) else False
	