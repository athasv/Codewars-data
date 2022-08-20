def grader(score):
    l = ["F", "F", "A", "B", "C", "D"]
    for i in l:
        if score > 1.0 or score < 0.6: return l[1]
        if 0.9 <= score <= 1.0: return l[2]
        if 0.8 <= score < 0.9: return l[3]
        if 0.7 <= score < 0.8: return l[4] 
        if 0.6 <= score < 0.7: return l[5]