

class GameOfLife():
   

    def __init__(self) -> None:
        self.board = []  # Representação do tabuleiro
        self.width = 10  # Largura do tabuleiro
        self.height = 10  # Altura do tabuleiro
        self.initialize_board()

    # Função para inicializar o tabuleiro com células vivas e mortas
    def initialize_board(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        
        #tabuleiro preenchido com células vivas
        self.board[3][4] = 1
        self.board[3][5] = 1
        self.board[4][3] = 1
        self.board[4][4] = 1
        self.board[5][4] = 1

    # Função para atualizar o estado do tabuleiro de acordo com as regras do Jogo da Vida
    def update_board(self):

        new_board = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                alive_neighbors = self.count_alive_neighbors(i, j)

                if self.board[i][j] == 1 and (alive_neighbors == 2 or alive_neighbors == 3):
                    new_board[i][j] = 1
                elif self.board[i][j] == 0 and alive_neighbors == 3:
                    new_board[i][j] = 1

        self.board = new_board

    def print_board(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))

    # Função para contar o número de células vizinhas vivas de uma célula específica
    def count_alive_neighbors(self, row, col) -> int:
        count = 0

        for i in range(max(0, row - 1), min(self.height, row + 2)):
            for j in range(max(0, col - 1), min(self.width, col + 2)):
                if (i, j) != (row, col) and i < self.height and j < self.width and self.board[i][j] == 1:
                    count += 1

        return count