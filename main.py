import queue
import random

class State:
    def __init__(self, board, goal, moves=0):
        #객체의 초기화 동작을 정의하는 magic method
        self.board = board
        self.moves = moves
        self.goal = goal

    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)

    def expand(self, moves):
        result = []
        i = self.board.index(0)
        if not i in [0, 1, 2]:
            result.append(self.get_new_board(i, i-3, moves))

        if not i in [0, 3, 6]:
            result.append(self.get_new_board(i, i-1, moves))

        if not i in [2, 5, 8]:
            result.append(self.get_new_board(i, i+1, moves))

        if not i in [6, 7, 8]:
            result.append(self.get_new_board(i, i+3, moves))

        return result

    def f(self):
        return self.h() + self.g()

    def h(self):
        # 제 위치에 있지 않은
        # 타일의 개수 카운
        return sum([1 if self.board[i] != self.goal[i] else 0 for i in range(8)])

    def g(self):
        # 시작 노드로부터의 거리
        # 트리에서는 레벨이 될듯
        return self.moves

    def __lt__(self, other):
    # x < y calls x.__lt__(y) (no override, just original)
        return self.f() < other.f()

    def __eq__(self, other):
        return self.board == other.board


    def __str__(self):
        return ("--------------- f(n) = " + str(self.f()) +"\n" +
               "--------------- h(n) = " + str(self.h()) +"\n" +
               "--------------- g(n) = " + str(self.g()) +"\n" +
                str(self.board[:3]) + "\n" + str(self.board[3:6]) +"\n"
                +str(self.board[6:9]))

def checksolveable(puzzleboard):
    inversion = 0

    for i in range(0, 8):
        tmp = puzzleboard[i]

        if tmp == 0:
            continue

        for j in range(i + 1, 9):
            if puzzleboard[j] == 0:
                continue

            if tmp > puzzleboard[j]:
                inversion = inversion + 1

    if inversion % 2 == 0:
        return True
    else:
        return False


def createrandompuzzle():
    puzzletmp = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while True:
        random.shuffle(puzzletmp)

        if checksolveable(puzzletmp):
            break

    return puzzletmp


puzzle = createrandompuzzle()
#puzzle = [1, 2, 3, 0, 4, 6, 7, 5, 8]
# 문제의 입력 2, 1, 0, 4, 6, 8, 3, 7, 5

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print("문제", puzzle)
open_queue = queue.PriorityQueue()
'''
Open Queue를 우선순위 큐로 만드는 이유

우선순위 큐 자료구조는 일반적인 큐와 달리, 데이터의 추가는 어떤 순서로
해도 상관이 없지만, 제거될 때는 가장 작은 값을 제거하는 특성을 지님
-> 내부적으로 데이터를 정렬된 상태로 보관하는 메커니즘이 내제

객체 번호가 가장 낮은것부터 pop하려는 듯

'''
open_queue.put(State(puzzle, goal))

closed_queue = []
moves = 0
check_tmp = 0;
while not open_queue.empty():
    current = open_queue.get()
    print(current)

    if current.board == goal:
        print("탐색 성공")
        break

    moves = current.moves + 1

    for state in current.expand(moves):
        if (state not in closed_queue):
            open_queue.put(state)
            check_tmp = check_tmp + 1
        closed_queue.append(current)



    print("counting : " + str(check_tmp));
else:
    print("탐색 실패")


