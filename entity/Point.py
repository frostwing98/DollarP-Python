
class Point:
    def __init__(self, x, y,id):
        self.x=x
        self.y=y
        self.id=id
    def __str__(self):
        return str(self.x)+" "+str(self.y)+" "+str(self.id)

