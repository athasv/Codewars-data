def better_than_average(class_points, your_points):
    # Your code here
    return True if your_points >= int(sum(class_points)/len(class_points)) else False