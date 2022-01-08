def abbrev_name(name:str) -> str:
	temp = [ i[0].upper() for i in name.split(" ")]
	return ".".join(temp)