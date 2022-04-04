def weather_info(t):
    temp = float((t - 32) * (5/9))
    return (str(temp) + " is above freezing temperature") if (temp > 0) else (str(temp) + " is freezing temperature")
