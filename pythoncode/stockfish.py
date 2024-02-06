import chess
import chess.engine


class Stockfish:
	def __init__(self):
		self.engine = chess.engine.SimpleEngine.popen_uci("D:\Matthias\Chess\ChessAPI\Python\stockfish\stockfish.exe")
		self.engine.configure({"Threads": 4})

	def getEval(self, board):
		info = self.engine.analyse(board, chess.engine.Limit(depth = 15))
		score = info["score"].relative
		isWhite = info["score"].turn
		nameLol = score.score()
		if nameLol == None:
			mateString = str(info["score"].relative)
			if (mateString[1] == "+") and (isWhite == True):
				return 1000
			if (mateString[1] == "-") and (isWhite == False):
				return 1000
			else:
				return -1000
		value = int(nameLol)

		if isWhite == False:
			value = value * -1
		return value

	def stopEngine(self):
		self.engine.quit()










