import copy
import collections
import random

'''
문제점 : openQueue를 리스트가 아닌 collections의 dequeue매서드를 이용해서 큐를 구현해야함
        why) 일반적인 리스트는 random access에 적합하여, 데이터가 많아지면 데이터를 앞에서 추가하거나 삭제할때
             전체 데이터를 하나하나씩 다 밀어야함. 복잡도 O(n)
             
리스트 말고, 문자열 비교로 하면 더 빨라질 가능성이 있을거 같음? 게다가 closedQueue같은 경우 딕셔너리로 구현하면 속도 개선있는듯
참고 : https://comdoc.tistory.com/entry/python-8-puzzle-problem-1-BFS-DFS

교재에서 처럼 클래스(State)에 넣고 했는데, 시간이 더 오래걸려서 해답이 나오지 않는건지 구현에 문제가 있는건지 해답이 나오질 않음
현재 객체를 이용하지 않고, 모든 퍼즐은 리스트로 핸들링중

'''
def displayPuzzle(puzzle):
    print(str(puzzle[:3]) + "\n" + str(puzzle[3:6]) + "\n" + str(puzzle[6:]) + "\n")

def makeRandomizePuzzle():
    puzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    while True:
        random.shuffle(puzzle)

        solveable = checkSolveable(puzzle)

        if solveable == True:
            return puzzle

    return random.shuffle(puzzle)

def checkSolveable(puzzle):
    inversion = 0

    for i in range(0, 8):

        if puzzle[i] == 0:
            continue

        current = puzzle[i]

        for j in range( i + 1, 9):
            if puzzle[j] == 0 :
                continue
            if current > puzzle[j]:
                inversion = inversion + 1
    
    if inversion%2 == 0:
        return True
    else :
        return False

def newPuzzleBody(puzzle, before, after):
    newPuzzleBody = copy.deepcopy(puzzle)
    newPuzzleBody[before], newPuzzleBody[after] = newPuzzleBody[after], newPuzzleBody[before]
    return newPuzzleBody

def expand(puzzle):
    result = []

    i = puzzle.index(0)

    if not i in [0, 1, 2]:
        result.append(newPuzzleBody(puzzle, i, i - 3))
            
    if not i in [0, 3, 6]:
        result.append(newPuzzleBody(puzzle,i, i - 1))

    if not i in [2, 5, 8]:
        result.append(newPuzzleBody(puzzle,i, i + 1))

    if not i in [6, 7, 8]:
        result.append(newPuzzleBody(puzzle,i, i + 3))
        
    return result



def BFS(puzzle, goal):
    openQueue = collections.deque([puzzle])

    closedQueue = []

    while len(openQueue) != 0:
        currentNode = openQueue.popleft()
        #print("현재 노드는", currentNode)

        if goal == currentNode :
            print("Answer is founded by bfs")
            displayPuzzle(currentNode)
            break

        closedQueue.append(currentNode)
        #print("closed 큐에는", closedQueue)

        for newNode in expand(currentNode):
            if (newNode in openQueue) or (newNode in closedQueue):
                continue
            else :
                openQueue.append(newNode)
        #print("새롭게 추가된 오픈 큐에는", openQueue)

def DFS(puzzle, goal):
    openStack = collections.deque([puzzle])

    closedStack = []

    while len(openStack) != 0:
        currentNode = openStack.pop()
        #print("현재 노드는", currentNode)

        if goal == currentNode :
            print("Answer is founded by dfs")
            displayPuzzle(currentNode)
            break

        closedStack.append(currentNode)
        #print("closed 큐에는", closedQueue)

        for newNode in expand(currentNode):
            if (newNode in openStack) or (newNode in closedStack):
                continue
            else :
                openStack.append(newNode)
        #print("새롭게 추가된 오픈 큐에는", openQueue)


firstPuzzle = makeRandomizePuzzle()
secondPuzzle = makeRandomizePuzzle()
thirdPuzzle = makeRandomizePuzzle()

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

displayPuzzle(firstPuzzle)
BFS(firstPuzzle, goal)
DFS(firstPuzzle, goal)

displayPuzzle(secondPuzzle)
BFS(secondPuzzle, goal)
DFS(secondPuzzle, goal)

displayPuzzle(thirdPuzzle)
BFS(thirdPuzzle, goal)
DFS(thirdPuzzle, goal)



