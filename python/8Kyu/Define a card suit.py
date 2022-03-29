def define_suit(card):
    if card.endswith("C"): return "clubs"
    if card.endswith("D"): return "diamonds"
    if card.endswith("H"): return "hearts"
    if card.endswith("S"): return "spades"