def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    pass # Don't get eaten!
    return "Alive!" if pontoon_distance / you_speed <= (shark_distance / shark_speed * (2 if dolphin else 1)) else "Shark Bait!"
    