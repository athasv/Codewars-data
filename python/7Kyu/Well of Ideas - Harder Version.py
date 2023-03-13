def well(arr):
    return "I smell a series!" if (str(arr).lower().count("good") > 2) else "Fail!" if not (str(arr).lower().count("good")) else "Publish!"