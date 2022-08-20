def add_length(str_):
    temp_dict = []
    for i in str_.split():
        temp_dict.append("{} {}".format(str(i), str(len(i))))
    return temp_dict
