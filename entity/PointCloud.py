import entity.Point as Point
from Processors.Pointprocessor import *
NumPoints=32
Origin=Point.Point(0, 0, 0)


class PointCloud:

    def __init__(self,name,points):
        self.name=name
        self.points = resample(points, NumPoints)
        self.points = scale(points)
        self.points = translateto(points, Origin)


