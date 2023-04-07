import unittest
from tetris import Tetris


class TestTetris(unittest.TestCase):

    def setUp(self):
        self.tetris = Tetris()

    def test_new_block(self):
        self.tetris.new_block()
        self.assertIsNotNone(self.tetris.block)
        self.assertIsNotNone(self.tetris.block_x)
        self.assertIsNotNone(self.tetris.block_y)

    def test_move_block_left(self):
        # test move block left without collision
        self.tetris.new_block()
        initial_x = self.tetris.block_x
        self.tetris.move_block_left()
        self.assertEqual(self.tetris.block_x, initial_x-1)

        # test move block left with collision
        self.tetris.block_x = 0
        initial_x = self.tetris.block_x
        self.tetris.move_block_left()
        self.assertEqual(self.tetris.block_x, initial_x)
        self.assertIsNotNone(self.tetris.block)

    def test_move_block_right(self):
        # test move block right without collision
        self.tetris.new_block()
        initial_x = self.tetris.block_x
        self.tetris.move_block_right()
        self.assertEqual(self.tetris.block_x, initial_x+1)

        # test move block right with collision
        self.tetris.block_x = self.tetris.width - len(self.tetris.block[0])
        initial_x = self.tetris.block_x
        self.tetris.move_block_right()
        self.assertEqual(self.tetris.block_x, initial_x)
        self.assertIsNotNone(self.tetris.block)

    def test_rotation(self):
        tetris = Tetris()
        # Test rotating the block clockwise
        tetris.block = [['*', ' ', ' '],
                        ['*', '*', '*']]
        tetris.block_x = 4
        tetris.block_y = 4
        tetris.rotate_block_clockwise()
        assert tetris.block == [['*', '*'],
                                ['*', ' '],
                                ['*', ' ']]
        # Test rotating the block anticlockwise
        tetris.block = [['*', '*', '*'],
                        ['*', ' ', ' ']]
        tetris.block_x = 0
        tetris.block_y = 0
        tetris.rotate_block_anticlockwise()
        assert tetris.block == [['*', ' '],
                                ['*', ' '],
                                ['*', '*']]


if __name__ == '__main__':
    unittest.main()
