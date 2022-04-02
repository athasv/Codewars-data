def validate_hello(greetings):
    import re
    temp_string = greetings.lower()
    temp = {"hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"}
    for i in temp:
        if i in temp_string:
            return True
    return False