import chess.pgn
import stockfish
import matplotlib.pyplot as plt
import math

class Plotter:
    def __init__(self):
        self.numbers = []
        self.middle = []
        self.sf = stockfish.Stockfish()

    def clamp(self, value, lower_limit, upper_limit):
        return max(min(value, upper_limit), lower_limit)
    
    def readGame(self, png):
        # Iterate through the moves
        node = png
        while node is not None:
            eval = self.sf.getEval(node.board())
            eval = self.clamp(eval, -1000, 1000)
            self.numbers.append(eval)
            self.middle.append(0)
            node = node.next()
        self.sf.stopEngine()
    
    def openPlot(self):
        plt.plot(self.numbers)
        plt.plot(self.middle)
        plt.xlabel('Move')
        plt.ylabel('Eval')
        plt.title('Chess Game Eval Curve')
        plt.autoscale()
        plt.tight_layout()
        plt.show()

    def calcBlunders(self):
        for i in range(1, len(self.numbers)):
            current = self.numbers[i]
            last = self.numbers[i - 1]
            diff = abs(current - last)
            if (diff >= 300):
                print(f"blunder on move {(i+1)/2} with diff {diff}")
