def leo(oscar):
    t = ["Leo finally won the oscar! Leo is happy", "Not even for Wolf of wallstreet?!", "When will you give Leo an Oscar?",  "Leo got one already!"]
    n = [88, 86]
    if oscar == n[0]: return t[0]
    if oscar == n[1]: return t[1]
    if oscar != n[0] and oscar != n[1] and oscar < n[0]: return t[2]
    if oscar > n[0]: return t[3]