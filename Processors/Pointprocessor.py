from entity import Point,PointCloud
import math
def resample( points, n):
    eta = PathLength(points) / (n - 1)
    delta = 0.0
    newpoints = [points[0]]
    length = len(points)
    i = 1
    while i < length:
        if points[i].id == points[i - 1].id:
            d = Distance(points[i - 1], points[i])
            if (delta + d) >= eta:
                qx = points[i - 1].x + ((eta - delta) / d) * (points[i].x - points[i - 1].x)
                qy = points[i - 1].y + ((eta - delta) / d) * (points[i].y - points[i - 1].y)
                q = Point.Point(qx, qy, points[i].id)
                newpoints.append(q)
                points.insert(i, q)
                length = length + 1
                delta = 0.0
            else:
                delta = delta + d
        i = i + 1

    if len(newpoints) == n - 1:
        p = Point.Point(points[length - 1].x, points[length - 1].y, points[length - 1].id);
        newpoints.append(p)

    return newpoints


def scale(points):
    minX = +float('inf')
    maxX = -float('inf')
    minY = +float('inf')
    maxY = -float('inf')
    for i in range(0, len(points)):
        minX = min(minX, points[i].x)
        minY = min(minY, points[i].y)
        maxX = max(maxX, points[i].x)
        maxY = max(maxY, points[i].y)
    size = max(maxX - minX, maxY - minY)
    newpoints = []
    for i in range(0, len(points)):
        qx = (points[i].x - minX) / size
        qy = (points[i].y - minY) / size
        newpoints.append(Point.Point(qx, qy, points[i].id))
    return newpoints


def translateto(points, pt):
    c = centroid(points)
    newpoints = []
    for i in range(0, len(points)):
        qx = points[i].x = pt.x - c.x
        qy = points[i].y + pt.y - c.y
        p = Point.Point(qx, qy, points[i].id)
        newpoints.append(p)
    return newpoints


def centroid( points):
    x = 0.0
    y = 0.0
    for i in range(0, len(points)):
        x = x + points[i].x
        y = y + points[i].y
    x = x / len(points)
    y = y / len(points)
    p = Point.Point(x, y, 0)
    return p


def PathLength(points):
    d = 0.0
    for i in range(1, len(points)):
        if points[i].id == points[i - 1].id:
            d = d + Distance(points[i - 1], points[i])
    return d


def Distance( p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return math.sqrt(dx * dx + dy * dy)