def cannons_ready(gunners):
	temp = [i for i in gunners.values() if i == 'nay']
	if len(temp) == 0: return 'Fire!'
	if len(temp) != 0: return 'Shiver me timbers!'