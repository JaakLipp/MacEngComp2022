import random
from shapely.geometry import Point

class Location():

    def __init__(self, max_x, max_y, min_x, min_y):
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = min_x
        self.min_y = min_y

    def get_random_location(self):
        random_point = Point([random.uniform(self.min_x, self.max_x), random.uniform(self.min_y, self.max_y)])
        return random_point
