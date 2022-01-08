def final_grade(exam, projects):
    if projects > 10 or exam > 90: return 100
    if projects >= 5 and exam > 75: return 90
    if projects >= 2 and exam > 50: return 75
    if projects < 2 or exam < 50: return 0
    if projects == 0 or exam == 0: return 0