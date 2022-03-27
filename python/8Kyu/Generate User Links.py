def generate_link(user):
    import urllib.parse
    return "http://www.codewars.com/users/{}".format(urllib.parse.quote(user))