class rectangule:
    def __init__(self, top_corner,lower_corner):
        self.top_corner= top_corner
        self.lower_corner= lower_corner

    def perimeter(self):
        base=abs(self.top_corner.x-self.lower_corner.x)
        height=abs(self.top_corner.y-self.lower_corner.y)
        return 2*(base+height)

    def area(self):
        base = abs(self.top_corner.x - self.lower_corner.x)
        height = abs(self.top_corner.y - self.lower_corner.y)
        return base*height

    def is_square(self):
        base = abs(self.top_corner.x - self.lower_corner.x)
        height = abs(self.top_corner.y - self.lower_corner.y)
        if base == height:
            return print("The figure is square")



