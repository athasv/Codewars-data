TIP = {
    'terrible': 0,
    'poor': 5,
    'good': 10,
    'great': 15,
    'excellent': 20
}


def calculate_tip(amount, rating):
    t = TIP.get(rating.lower(), 'Rating not recognised')
    return t if isinstance(t, str) else __import__("math").ceil((amount / 100) * t)
