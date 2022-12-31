def html_special_chars(data): 
    temp = {'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}
    return "".join( (temp.get(_,_)) for _ in data)