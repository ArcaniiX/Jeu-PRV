import matplotlib.pyplot as plt

class Board():

    def __init__(self):
        self.x = 5
        self.y = 5

    def __str__(self):
        plt.grid()
        plt.plot([0,self.x],[0,0],"black")
        plt.plot([self.x,self.x],[0,self.y],"black")
        plt.plot([self.x,0],[self.y,self.y],"black")
        plt.plot([0,0],[self.y,0],"black")