def animals(heads, legs):
    if(heads==0 and legs == 0):
        return (0,0)
    elif(heads<=0 or legs<=0):
        return 'No solutions'
    elif(heads>=1000 or legs>=1000):
        return 'No solutions'
    elif(heads*2 == legs):
        return (heads,0)
    elif(heads*4 == legs):
        return (0,heads)
    else:
        animals = heads
        cows = ((legs - heads * 2)/4)*2
        chicken = animals - cows
        if(chicken<=0 or cows<=0):
            return 'No solutions'
        else:
            if(chicken.is_integer()):
                return(chicken,cows)
            else: 
                return 'No solutions'
    