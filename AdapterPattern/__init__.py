# 结构型设计模式的主要用途是将一种对象改装为另一种对象

# 鸭子的简单描述
class Duck:
    def quack(self):
        # 会呱呱叫
        print("Quack")

    def fly(self):
        # 飞的能力
        print("I'm flying")


# 火鸡的简单描述
class Turkey:
    def gobble(self):
        # 不会呱呱叫，只会咯咯叫
        print("Gobble gobble")

    def fly(self):
        # 飞的能力 但是飞不远
        print("I'm flying a short distance")


class TurkeyAdapter(Duck):
    turkey = Turkey()  # 这里实际使用的是火鸡对象

    # 实现鸭子对象拥有的quack方法
    def quack(self):
        self.turkey.gobble()

    def fly(self):
        # 假设火鸡比鸭子飞的短，为了模拟鸭子的动作，多飞几次
        for i in range(5):
            self.turkey.fly()



def createDuck(duck):
    duck.quack()
    duck.fly()



# test
duck = Duck()
createDuck(duck)

turkey = TurkeyAdapter()
createDuck(turkey)
