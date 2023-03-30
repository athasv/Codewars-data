def middle_me(N, X, Y): 
    temp_str = Y*N
    if len(temp_str)%2==0:
        _ = round(len(temp_str)/2)
        return "{}".format(temp_str[:_]+X+temp_str[_:])
    return "{}".format(X)