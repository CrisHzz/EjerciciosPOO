class circle:
    def __init__(self,center,radio):
        self.center=center
        self.radio=radio
    def area(self):
        return 3.1416*(self.radio**2)
    def perimeter(self):
        return 2*3.1416*self.radio
    def is_inside(self,point):
        if (self.center.x-point.x)**2+(self.center.y-point.y)**2<=self.radio**2:
            return True
        else:
            return False
