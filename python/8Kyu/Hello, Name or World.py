def hello(name=""):
    return "Hello, World!" if "".__eq__(name) else "Hello, {}!".format((name.lower()).capitalize()) 