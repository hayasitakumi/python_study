from board import Board
from dfs import dfs

class SearchProblem:
    '''探索問題を定義する抽象クラス'''
    def get_start_state(self):
        '''初期状態を返す関数'''
        raise NotImplementedError
    
    def next_states(self, state):
        '''与えられた状態 state から遷移できる状態のリストを返す関数'''
        raise NotImplementedError

    def is_goal(self, state):
        '''与えられた状態 state がゴールかどうかを True/False で返す関数'''
        raise NotImplementedError


class Sudoku(SearchProblem):
    def __init__(self, board):
        self.board = board
    
    def get_start_state(self):
        return self.board
    
    def is_goal(self, board):
        for x in range(0, 9):
            for i in range(1, 9):
                if self.board.data[x].count(i) > 1:
                    return False
        
        return False
 
    def next_states(self, board):
        pass


if __name__ == '__main__':
    problem_data = \
        [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    solution_data = \
        [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    board = Board(problem_data)
    sudoku = Sudoku(board)
    print(sudoku.is_goal(solution_data))
    
    # boards = dfs(sudoku)
    # for i, board in enumerate(boards):
    #     print('\nSTEP %d' % i)
    #     print(board)
    # assert boards[-1].data == solution_data
