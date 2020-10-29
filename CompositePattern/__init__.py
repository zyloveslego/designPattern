# 组合模式在 Python 代码中很常见， 常用于表示与图形打交道的用户界面组件或代码的层次结构。
# 根节点操作叶子节点和枝干节点，叶子和枝干需要实现相同的接口


from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def operation(self, depth):
        pass

    @abstractmethod
    def add(self, c):
        pass

    @abstractmethod
    def remove(self, c):
        pass

    @abstractmethod
    def get_child(self, index):
        pass


class Composite(Component):
    def __init__(self, name):
        Component.__init__(self, name)
        self.children = []

    def operation(self, depth):
        print(depth)
        strtemp = ''
        for i in range(depth):
            strtemp = strtemp+'-'
        print(strtemp+self.name)
        for comp in self.children:
            comp.operation(depth+2)

    def add(self, c):
        self.children.append(c)

    def remove(self, c):
        self.children.remove(c)

    def get_child(self, index):
        return self.children[index]


class Leaf(Component):
    def operation(self, depth):
        print(depth)
        strtemp = ''
        for i in range(depth):
            strtemp = strtemp+'-'
        print(strtemp+self.name)

    def add(self, c):
        print('不能添加下级节点！')

    def remove(self, c):
        print('不能删除下级节点！')

    def get_child(self, index):
        print('没有下级节点！')


class Client:
    @staticmethod
    def main():
        # 生成树根
        root = Composite("root")
        # 根上长出2个叶子
        root.add(Leaf('leaf A'))
        root.add(Leaf('leaf B'))
        # 根上长出树枝Composite X
        comp = Composite("Composite X")
        comp.add(Leaf('leaf XA'))
        comp.add(Leaf('leaf XB'))
        root.add(comp)
        # 根上长出树枝Composite X
        comp2 = Composite("Composite XY")
        # Composite X长出2个叶子
        comp2.add(Leaf('leaf XYA'))
        comp2.add(Leaf('leaf XYB'))
        root.add(comp2)
        # 根上又长出2个叶子,C和D,D没长好,掉了
        root.add(Leaf('Leaf C'))
        leaf = Leaf("Leaf D")
        root.add(leaf)
        root.remove(leaf)
        # 展示组织
        root.operation(1)


if __name__ == '__main__':
    Client.main()