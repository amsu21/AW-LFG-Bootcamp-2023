class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        point1 = Point(10, 20)
        
        # GET THE REPR OF P1
        point1_repr = repr(point1)
        
        point2 = eval(point1_repr)
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"