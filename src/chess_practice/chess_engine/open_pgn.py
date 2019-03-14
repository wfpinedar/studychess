import os
import chess.pgn
import chess.svg

path = os.path.dirname(os.path.abspath(__file__))


pgn = open(os.path.join(path, 'src/chess_practice/chess_engine/db.pgn'), encoding="ISO-8859-1")

#for game in pgn:
#    print(chess.pgn.Mainline(pgn))
first_game = chess.pgn.read_game(pgn)
second_game = chess.pgn.read_game(pgn)
#
# first_game.headers["Event"]
# second_game.headers["Event"]
#
#
# board = second_game.board()
# squares = board.attacks(chess.F6)
# chess.svg.board(board=board, squares=squares)
# [head for head in second_game.headers] headers
# [print(i) for i in first_game.variations] Variaciones.

# print(board)
