import unittest
from board import Board

# https://en.wikipedia.org/wiki/Sudoku
PROBLEM = ('53  7    \n'
           '6  195   \n'
           ' 98    6 \n'
           '8   6   3\n'
           '4  8 3  1\n'
           '7   2   6\n'
           ' 6    28 \n'
           '   419  5\n'
           '    8  79')
SOLUTION = ('534678912\n'
            '672195348\n'
            '198342567\n'
            '859761423\n'
            '426853791\n'
            '713924856\n'
            '961537284\n'
            '287419635\n'
            '345286179')

def text_to_data(text):
    data = []
    for line in text.splitlines():
        assert len(line) == 9
        data.append(list(map(int, line.replace(' ', '0'))))
    return data


class TestBoard(unittest.TestCase):
    def test_not_filled(self):
        board = Board(text_to_data(PROBLEM))
        self.assertFalse(board.filled())
    
    def test_filled(self):
        board = Board(text_to_data(SOLUTION))
        self.assertTrue(board.filled())

    def test_verify_problem(self):
        board = Board(text_to_data(PROBLEM))
        self.assertTrue(board.verify())

    def test_verify_solution(self):
        board = Board(text_to_data(SOLUTION))
        self.assertTrue(board.verify())

    def test_verify_modified_board1(self):
        '''duplicate digits in the same column'''
        mod = text_to_data(PROBLEM)
        mod[0][0] = 4
        board = Board(mod)
        self.assertFalse(board.verify())

    def test_verify_modified_board2(self):
        '''duplicate digits in the same row'''
        mod = text_to_data(PROBLEM)
        mod[8][3] = 7
        board = Board(mod)
        self.assertFalse(board.verify())

    def test_verify_modified_board3(self):
        '''duplicate digits in the same 3x3 block'''
        mod = text_to_data(PROBLEM)
        mod[0][6] = 6
        board = Board(mod)
        self.assertFalse(board.verify())

    def test_get_allowed_digits_returns_list(self):
        board = Board(text_to_data(PROBLEM))
        self.assertIsInstance(board.get_allowed_digits(3, 3), list)

    def test_get_allowed_digits_0_0(self):
        board = Board(text_to_data(PROBLEM))
        self.assertEqual(board.get_allowed_digits(0, 0), [])

    def test_get_allowed_digits_2_0(self):
        board = Board(text_to_data(PROBLEM))
        self.assertEqual(sorted(board.get_allowed_digits(2, 0)), [1, 2])

    def test_get_allowed_digits_0_2(self):
        board = Board(text_to_data(PROBLEM))
        self.assertEqual(sorted(board.get_allowed_digits(0, 2)), [1, 2, 4])

    def test_move_actually_puts_digit(self):
        board = Board(text_to_data(PROBLEM))
        new_board = board.move(1, 2, 4)
        self.assertEqual(new_board.data[1][2], 4)

    def test_move_does_not_change_original_board(self):
        board = Board(text_to_data(PROBLEM))
        _ = board.move(1, 2, 4)
        self.assertEqual(board.data[1][2], 0)

    def test_move_leaves_other_digits_unchanged(self):
        board = Board(text_to_data(PROBLEM))
        ref_board = Board(text_to_data(PROBLEM))
        new_board = board.move(1, 2, 4)
        self.assertTrue(all(ref_board.data[x][y] == new_board.data[x][y]
                            for x in range(9) for y in range(9)
                            if (x, y) != (1, 2)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
