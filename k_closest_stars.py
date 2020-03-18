import math 

class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x,y,z
    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 +self.y**2 + self.z**2)
    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance
