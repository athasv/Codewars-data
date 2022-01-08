def how_much_i_love_you(n):
    temp = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return temp[(n % len(temp)) -1] 