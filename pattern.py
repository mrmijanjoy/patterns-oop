import queue  #Queue pattern
import os  #Command pattern
import types  #Strategy pattern
from copy import deepcopy  #ProtoType pattern
import time  #ProtoType pattern


# QUEUE

class Car:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(self.name)


obj1 = Car("volvo")
obj2 = Car("bmw")
obj3 = Car("crysler")
obj4 = Car("opel")

q = queue.LifoQueue()
q.put(obj1)
q.put(obj2)
q.put(obj3)
q.put(obj4)

while not q.empty():
    obj = q.get()

# COMMAND PATTERN

class moveFileCommand(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        os.rename(self.src, self.dst)

    def undo(self):
        os.rename(self.src, self.dst)

stack = []
stack.append(moveFileCommand('hello.txt', 'hey.txt'))
stack.append(moveFileCommand('no.txt', 'yeah.txt'))

stack.pop().undo()
stack.pop().undo()


# STRATEGY PATTERN

class strategy:
    def __init__(self, func = None):
        if func is not None:
            self.execute = types.MethodType(func, self)

        def execute(self):
            print(self.name)

def executeOne(self):
    print("Hi")

def executeTwo(self):
    print("Hello")

obj = strategy(executeOne())
obj.execute()


# SINGLETON

class car:
    _instance = None

    def getInstance(self):
        if car._instance == None:
            car()
        return car._instance

    def __init__(self):
        if car._instance != None:
            raise Exception("Singleton")
        else:
            car._instance = self

obj = car()
print(obj)


# STATE PATTERN

class computerState:
    name = "state"

    def switch(self, state):
        self.__class__ = state

    def __str__(self):
        return self.name

class on(computerState):
    name = "on"

class off(computerState):
    name = "off"

class hibernate(computerState):
    name = "hibernate"

class suspend(computerState):
    name = "suspend"

class computer:
    def __init__(self):
        print("Computer")
        self.state = off()

    def change(self, state):
        self.state.switch(state)

obj = computer()
obj.change(on)


# FACADE PATTERN

class CPU:
    def execute(self):
        print('Run command')

class Memory:
    def load(self):
        print('Load in memory')

class Disk:
    def read(self):
        print('Read from disk')


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.mem = Memory()
        self.disk = Disk()

    def start(self):
        self.cpu.execute()
        self.disk.read()
        self.mem.load()

    def stop(self):
        self.cpu.execute()


computer = ComputerFacade()
computer.start()
computer.stop()


# TEMPLATE PATTERN

class MakeFood:
    def prepare(self):
        pass

    def collect(self):
        pass

    def cook(self):
        pass

class MakePizza(MakeFood):
      def prepare(self):
          print("Prepare dough")
          print("Cut tomatoes...")

      def collect(self):
          print("Get tomatoes, dough etc")

      def cook(self):
          print("Baking pizza")

class MakeSpaghetti(MakeFood):
    def prepare(self):
        print("Preparing..")

    def collect(self):
        print("Prepare dough..")

    def cook(self):
        print("Wait for spaghetti to cook")

obj1 = MakePizza()
obj1.prepare()
obj1.collect()
obj1.cook()


# ITERATOR PATTERN

class Car:
    pass

numbers = [Car(),Car(),Car(),Car()]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))


# PROTOTYPE PATTERN

class Prototype(object):
    def clone(self):
        return deepcopy(self)

class NetworkConnector(Prototype):
    def __init__(self):
        self.name = "expensive method here"
        time.sleep(5)
        print("object created")

obj = NetworkConnector()
print(obj.name)

obj2 = obj.clone()
print(obj2.name)