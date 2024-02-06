import requests
import chess
import chess.pgn
import io

class Request:
	def __init__(self, name):
		self.api_url = f'https://api.chess.com/pub/player/{name}/games/2024/02/pgn'
		self.headers = {'User-Agent': f'matthias123456ziegler@gmail.com'}

	def getAllGames(self):
		response = requests.get(self.api_url, headers=self.headers)
		# Check if the request was successful (status code 200)
		if response.status_code == 200:
			return response.text	
		else:
			return None
		
	def getSignleGame(self, id):
		multipgn = io.StringIO(self.getAllGames())

		while True:
			pgn = chess.pgn.read_game(multipgn)
			header = pgn.headers["Link"]
			if id in header:
				return pgn
			if pgn is None:
				break
			
