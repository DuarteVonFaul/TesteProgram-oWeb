from services.gameOfLife import GameOfLife
from flask import render_template, request, jsonify


def init(app):

    game = GameOfLife()

    @app.route('/game-of-life')
    def index():
        return render_template('questao_02.html', width=game.width, height=game.height)

    # Rota para atualizar o estado do tabuleiro
    @app.route('/game-of-life/update_board', methods=['POST'])
    def update_board_route():
        game.update_board()
        return jsonify(board=game.board)

    # Rota para definir o estado inicial do tabuleiro
    @app.route('/game-of-life/initialize_board', methods=['POST'])
    def initialize_board_route():
        game.initialize_board()
        return jsonify(board=game.board)
