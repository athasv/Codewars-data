def get_drink_by_profession(param):
    dic = {"Jabroni": "Patron Tequila",
                "School Counselor": "Anything with Alcohol",
                "Programmer": "Hipster Craft Beer",
                "Bike Gang Member": "Moonshine",
                "Politician": "Your tax dollars",
                "Rapper": "Cristal"}
    return dic[param.title()] if param.title() in dic else "Beer"