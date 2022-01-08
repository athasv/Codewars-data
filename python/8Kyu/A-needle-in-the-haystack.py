def find_needle(haystack:str) -> str:
    temp = [i for i,j in enumerate(haystack) if j == "needle"]
    return "found the needle at position {}".format(haystack.index("needle"))
