def array(string):
    return ' '.join(string.split(',')[1:-1]).replace(',',' ') or None