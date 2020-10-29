# 桥接模式，用我自己的理解是把类作为参数传递给抽象类体系，这个传递的类是实现类，里面实现了抽象类需要的方法，由抽象类调用

class Eng:
    def run(self, name):
        print("my name is: {}".format(name))


class Chi:
    def run(self, name):
        print("我叫: {}".format(name))


class Bridge:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def speak(self):
        self.language.run(self.name)


if __name__ == '__main__':
    eng_student = Eng()
    Bridge("Tony", eng_student).speak()
    chi_student = Chi()
    Bridge("孙老板", chi_student).speak()

