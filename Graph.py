from numpy import ComplexWarning
import numpy as np
import matplotlib.pyplot as plt

class graph:
    global vals
    vals = []

    def __init__(self, equation, neg=-100, pos=100, step=0.1):
        self.equation = equation
        self.__x, self.__y = [], []
        self.pos = pos + step
        self.neg = neg
        self.step = step
        while self.neg < self.pos:
            self.__x.append(self.neg)
            self.neg += self.step
        for x in self.__x:
            try:
                self.__y.append(eval(self.equation))
            except ComplexWarning:
                pass
            except ZeroDivisionError:
                for y in range(int(self.neg / 2), int(self.pos) / 2):
                    self.__x.append(self.__x)
                    self.__y.append(y)
        self.__x = np.array(self.__x)
        self.__y = np.array(self.__y)
        plt.plot(self.__x, self.__y)
        plt.ylabel("Y-axis")
        plt.xlabel("X-axis")

    #Show the Graph
    def display(self): plt.show()

    #Getters
    def getX(self): return self.__x
    
    def getY(self): return self.__y