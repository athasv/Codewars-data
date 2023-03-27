def longest_word(string_of_words):
    temp = string_of_words.split()
    return sorted(temp, key = len)[-1]