import collections
import queue

class Num:
    def __init__(self, member):
        self.member = member

    def __lt__(self, other):
        print("lt magic method call!\n")
        return self.member < other.member

    def __eq__(self, other):
        print("eq magic method call!\n")
        return self.member == other.member

    def __ne__(self, other):
        print("ne magic method call!\n")
        return self.member != other.member


num1 = Num(1)
num2 = Num(2)

#numList = [num1, num2]
testQueue = queue.PriorityQueue()
testQueue.put(num1)
testQueue.put(num2)

num3 = Num(3)
testQueue.put(num3)
#num1 < num2
'''
num1 != num2

if num3 in numList:
    print("in here\n")

if num3 not in numList:
    print("not in here\n")
'''
testQueue.get()
testQueue.get()
#testQueue.get()