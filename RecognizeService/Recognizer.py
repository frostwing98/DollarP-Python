from entity import Point,PointCloud,Result
from Processors.Pointprocessor import *
import math
import datetime

NumPoints = 32
Origin = Point.Point(0, 0, 0)
class Recognizer:

    pointclouds = []
    pc=PointCloud.PointCloud("T",[Point.Point(30,7.0,1),Point.Point(103,7,1),Point.Point(66,7,2),Point.Point(66,87,2)])
    pointclouds.append(pc)

    def recognize(self,points):
        p = [Point.Point(30, 7, 1), Point.Point(103, 7, 1), Point.Point(66, 7, 2), Point.Point(66, 87, 2)]
        t0=datetime.datetime.now()
        points = resample(points,NumPoints)
        points = scale(points)
        points = translateto(points,Origin)
        b = float('inf')
        u = -1
        for i in range (0,len(self.pointclouds)):
            d=self.greedycloudmatch(points,self.pointclouds[i])
            if d<b:
                b = d
                u = i
        t1 = datetime.datetime.now()
        if u==-1:
            r1 = Result.Result("No match.", 0.0, t1 - t0)
            r = r1
        else:
            r2 = Result.Result(self.pointclouds[u].name, max((b - 2.0) / -2.0, 0.0), t1 - t0)
            r = r2
        return r

    def greedycloudmatch(self,points,P):
        e = 0.50
        step = int(math.floor(math.pow(len(points),1.0-e)))
        minimum = float('inf')

        for i in range(0,len(points),step):
            d1 = self.clouddistance(points,P.points,i)
            d2 = self.clouddistance(P.points,points,i)
            minimum=min(minimum,min(d1,d2))
        return minimum

    def clouddistance(self,pts1,pts2,start):
        matched=[]
        for k in range (0,len(pts1)):
            matched.append(0)
        sum=0
        i=start
        while i!=start:
            index=-1
            min=2147483647
            for j in range(0,len(matched)):
                if matched[j]==0:
                    d=PointCloud.PointCloud.Distance(pts1[i],pts2[j])
                    if d<min:
                        min=d
                        index=j
            matched[index]=1
            weight=1-((i-start+len(pts1))%len(pts1))/len(pts1)
            sum=sum+weight*min
            i=(i+1)%len(pts1)
        return sum


