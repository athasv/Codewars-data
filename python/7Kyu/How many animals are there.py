def count_animals(sentence):
    return sum(int(s) for s in sentence.split() if s.isdigit())