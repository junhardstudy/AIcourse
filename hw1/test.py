from collections import deque
from random import randint


def exchange(board: str, prev_pos: int, new_pos: int) -> str:
    new_board = list(board)
    new_board[prev_pos], new_board[new_pos] = new_board[new_pos], new_board[prev_pos]
    return ''.join(new_board)


def expand(board: str) -> list:
    result = []
    position = board.index('0')
    if position not in (0, 1, 2):  # UP
        result.append(exchange(board, position, position - 3))
    if position not in (0, 3, 6):  # LEFT
        result.append(exchange(board, position, position - 1))
    if position not in (2, 5, 8):  # RIGHT
        result.append(exchange(board, position, position + 1))
    if position not in (6, 7, 8):  # DOWN
        result.append(exchange(board, position, position + 3))
    return result


def pprint(board: str):
    print(' '.join(board[:3]) + '\n' +
          ' '.join(board[3:6]) + '\n' +
          ' '.join(board[6:]) + '\n' +
          '-----')


def randomize_start() -> str:
    board = []
    while not is_solvable(board):
        board = []
        while len(board) != 9:
            temp = str(randint(0, 8))
            if temp not in board:
                board.append(temp)
    return ''.join(board)


def is_solvable(board: list) -> bool:
    if not board:
        return False
    inversion = 0
    for i in range(len(board) - 1):
        if board[i] == '0':
            continue
        for j in range(i + 1, len(board)):
            if board[j] == '0':
                continue
            if board[i] > board[j]:
                inversion += 1
    return True if inversion % 2 == 0 else False


def bfs(start: str, goal: str) -> dict:
    que = deque()
    que.append(start)
    marked = {start: None}
    while que and (current := que.popleft()) != goal:
        for state in expand(current):
            if state not in marked:
                marked[state] = current
                que.append(state)
    return marked


def print_path(start: str, goal: str, marked):
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = marked[node]
    path.append(start)
    for each in path[::-1]:
        pprint(each)


def main():
    # start = '123506784'
    #start = randomize_start()
    start = '571326084'
    goal = '123456780'
    marked = bfs(start, goal)
    # marked = dfs(start, goal)
    print_path(start, goal, marked)
    print(start)
    print(len(marked))


if __name__ == '__main__':
    main()