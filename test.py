from collections import namedtuple

Point2d = namedtuple('point2d', ['x', 'y'])
Point3d = namedtuple('point3d', ['x', 'y', 'z'])

def make_point_3d(pt):
    match pt:
        case (x, int(y)):
            return Point3d(x, y, 0)
        case (x, y, z):
            return Point3d(x, y, z)
        case Point2d(x, y):
            return Point3d(x, y, 0)
        case Point3d(_, _, _):
            return pt
        case _:
            raise TypeError("not a point we support")

if(__name__ == '__main__'):
    p1 = ('1', 2)
    p2 = (1, 2, 3)
    p3 = Point2d(1, 2)
    p4 = Point3d(1, 2, 3)
    p5 = ('1', '2')
    print('Caso 1', make_point_3d(p1))
    print('Caso 2', make_point_3d(p2))
    print('Caso 3', make_point_3d(p3))
    print('Caso 4', make_point_3d(p4))
    print('Caso 5', make_point_3d(p5))  # Deve dar erro
    
