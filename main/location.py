import random
from shapely.geometry import Point

class Location():

    def __init__(self):
        self.max_x = int(input("Enter the maximum longitude you are sailing: "))
        self.max_y = int(input("Enter the maximum latitude you are sailing: "))
        self.min_x = int(input("Enter the minimum longitude you are sailing: "))
        self.min_y = int(input("Enter the minimum latitude you are sailing: "))

    def get_random_location(self):
        random_point = Point([random.uniform(self.min_x, self.max_x), random.uniform(self.min_y, self.max_y)])
        return random_point
