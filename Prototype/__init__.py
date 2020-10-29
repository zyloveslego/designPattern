# 如果想根据现有的对象复制出新的对象并对其修改

# copy.copy
# copy.deepcopy

# 另一种方法


class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Point(1, 2)
point2 = point1.__class__(3, 4)

print(point1)
print(point2)
