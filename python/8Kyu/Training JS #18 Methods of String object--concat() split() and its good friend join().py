def split_and_merge(string_, separator):
    if(separator != ""):
        x = ''
        for i in string_.split(" "):
            x = x + ' ' + separator.join(i)
    return x.strip(" ")