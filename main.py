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
        #평가 메서드
        return self.h() + self.g()

    def h(self):
        # 제 위치에 있지 않은
        # 타일의 개수 카운트
        return sum([1 if self.board[i] != self.goal[i] else 0 for i in range(8)])

    def g(self):
        # 시작 노드로부터의 거리
        # 트리에서는 레벨이 될듯
        return self.moves

    def __lt__(self, other):
        # x < y calls x.__lt__(y) (no override, just original) magic method
        # which is invoked when priorityQueue.put() method is called
        return self.f() < other.f()

    def __eq__(self, other):
        # x == y calls x.__eq__(y) magic method which is invoked when
        # compare operation (==, in) is called
        # 더불어서, 해당 magic method가 없다면 트리 깊이가 깊어질 때
        # if state not in closed_queue: 구문 수행시 board list 값을 비교해야 하는데
        # 해당 magic method가 없다면 객체 자체를 비교하게
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

def hwsolve():
    puzzle = createrandompuzzle()
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    print("---- initial state ----")
    open_queue = queue.PriorityQueue()

    '''
    Open Queue를 우선순위 큐로 만드는 이유

    우선순위 큐 자료구조는 일반적인 큐와 달리, 데이터의 추가는 어떤 순서로
    해도 상관이 없지만, 제거될 때는 가장 작은 값을 제거하는 특성을 지님
    -> 내부적으로 데이터를 정렬된 상태로 보관하는 메커니즘이 내제

    현재 magic method __lt__에 의해서 평가함수의 값이 가장 낮은 순으로
    정렬되도록 되어있음 

    그러면 값이 저장될 때부터 오름차순으로 저장되는건가??
    '''
    tmp = State(puzzle, goal)
    print(tmp)
    open_queue.put(tmp)

    closed_queue = []
    moves = 0

    while not open_queue.empty():
        current = open_queue.get()

        if current.board == goal:
            print("탐색 성공")
            print(current)
            break

        moves = current.moves + 1

        for state in current.expand(moves):
            if (state not in closed_queue):
                open_queue.put(state)
                # 큐에 넣을 때, 평가함수 값이 가장 낮은게 바로 다음
                # 탐색 순위가 되도록 함
            closed_queue.append(current)

    else:
        print("탐색 실패")


for i in range(0, 3):
    hwsolve()



