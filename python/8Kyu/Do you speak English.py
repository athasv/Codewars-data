def sp_eng(sentence): 
    # your code here
    return True if __import__("re").search(r'english',sentence.lower()) else 0