import random


class Tetris:
    def __init__(self):
        self.width = 12
        self.height = 12
        self.board = [[' ' for _ in range(self.width)]
                      for _ in range(self.height)]
        self.block = None
        self.block_x = 0
        self.block_y = 0

    def new_block(self):
        blocks = [
            [['*', '*', '*', '*']],
            [['*', '*', '*'], [' ', '*', ' ']],
            [['*', '*', '*'], ['*', ' ', ' ']],
            [['*', '*'], ['*', '*']],
            [['*', '*'], [' ', '*', '*']],
            [[' ', '*'], ['*', '*', '*']],
            [['*', ' '], ['*', '*', '*']]
        ]
        self.block = random.choice(blocks)
        self.block_x = self.width // 2 - len(self.block[0]) // 2
        self.block_y = 0

    def move_block_down(self):
        if not self.check_collision(self.block_x, self.block_y + 1, self.block):
            self.block_y += 1
        else:
            self.freeze_block()

    def drop_block(self):
        while not self.check_collision(self.block_x, self.block_y + 1, self.block):
            self.block_y += 1
        self.freeze_block()

    def move_block_left(self):
        if not self.check_collision(self.block_x - 1, self.block_y, self.block):
            self.block_x -= 1

    def move_block_right(self):
        if not self.check_collision(self.block_x + 1, self.block_y, self.block):
            self.block_x += 1

    def check_collision(self, x, y, block):
        for i in range(len(block)):
            for j in range(len(block[i])):
                if i + y >= len(self.board) or j + x < 0 or j + x >= len(self.board[i + y]):
                    if block[i][j] != ' ':
                        return True
                elif block[i][j] != ' ' and self.board[i + y][j + x] != ' ':
                    return True
        return False

    def freeze_block(self):
        for i in range(len(self.block)):
            for j in range(len(self.block[i])):
                if i + self.block_y >= 0:
                    self.board[i + self.block_y][j +
                                                 self.block_x] = '*' if self.block[i][j] != ' ' else ' '
        self.new_block()
        if self.check_collision(self.block_x, self.block_y, self.block):
            print('\n' * 50)
            print('GAME OVER')
            exit()

    def run_game_loop(self):
        self.new_block()
        while True:
            print('\n' * 50)
            print('SCORE:', sum([row.count('*') for row in self.board]))
            print('Press "q" to quit')
            print('Press "a" to move left')
            print('Press "d" to move right')
            print('Press " " to move down')
            print('Press "w" to rotate clockwise')
            print('Press "s" to rotate anticlockwise')
            print('Press "z" to drop')
            print('\n'.join([''.join(row)
                  for row in (self.get_board_with_current_block())]))
            command = input("enter the command: ")
            if command == 'q':
                break
            elif command == 'a':
                self.move_block_left()
            elif command == 'd':
                self.move_block_right()
            elif command == ' ':
                self.move_block_down()
            elif command == 'w':
                self.rotate_block_clockwise()
            elif command == 's':
                self.rotate_block_anticlockwise()
            elif command == 'z':
                self.drop_block()
            else:
                print('invalid input')

    def rotate_block_clockwise(self):

        rotated_block = []
        for i in range(len(self.block[0])):
            rotated_row = []
            for j in range(len(self.block)):
                rotated_row.append(self.block[len(self.block) - j - 1][i])
            rotated_block.append(rotated_row)
        if not self.check_collision(self.block_x, self.block_y, rotated_block):
            self.block = rotated_block

    def rotate_block_anticlockwise(self):
        rotated_block = []
        for i in range(len(self.block[0])):
            rotated_row = []
            for j in range(len(self.block)):
                rotated_row.append(self.block[j][len(self.block[0]) - i - 1])
            rotated_block.append(rotated_row)
        if not self.check_collision(self.block_x, self.block_y, rotated_block):
            self.block = rotated_block

    def get_board_with_current_block(self):
        board_copy = [row[:] for row in self.board]
        for i in range(len(self.block)):
            for j in range(len(self.block[i])):
                if i + self.block_y >= 0:
                    board_copy[i + self.block_y][j + self.block_x] = \
                        '*' if board_copy[i + self.block_y][j + self.block_x] == ' ' and \
                        (self.block[i][j] != ' ') else board_copy[i + self.block_y][j + self.block_x]
        return ['|' + ''.join(row) + '|' for row in board_copy]


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run_game_loop()
