# write the function is_anagram
def is_anagram(test, original):
    return set(test.lower()) == set(original.lower()) and len(test) == len(original)