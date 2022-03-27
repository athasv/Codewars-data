def validate(u, p):
    temp = Database()
    return "Wrong username or password!" if "||" in u+p and "//"  in u+p else temp.login(u,p)