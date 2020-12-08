# Reference
#https://github.com/aimacode/aima-pseudocode/tree/master/md

from state import State
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue


def DLS(given_state, n, depth):
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = Queue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        
        #print(current_node.depth)
        
        max_depth = current_node.depth #current depth
        explored.append(current_node.state)
        
        if max_depth >= depth:
            continue #go to the next branch
        
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return (False, len(explored))
    
def IDS(given_state , n):
    for depth in range(31): # 0 ~ 30
        (result,length) = DLS(given_state, n ,depth)
        if result != False:
            return result, length
        

def RBFS(given_state , n):
    return []

def UniformCostSearch(given_state , n):
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = PriorityQueue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                pass
        pass

#Breadth-first Search
def BFS(given_state , n):
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = Queue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        explored.append(current_node.state)
   
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return (("Couldn't find solution in the BFS."), len(explored))

#Depth-first Search with limited depth
def DFS(given_state , n): 
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = LifoQueue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        max_depth = current_node.depth #current depth
        explored.append(current_node.state)
        
        if max_depth == 20:
            continue #go to the next branch

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return (("Couldn't find solution in the limited depth."), len(explored))
    
def Greedy(given_state , n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    #root.evaluation()
    evaluation = root.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
    frontier.put((evaluation[0], counter, root)) #based on greedy evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
                frontier.put((evaluation[0], counter, child)) #based on greedy evaluation
    return


def AStar_search(given_state , n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    evaluation = root.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
    frontier.put((evaluation[1], counter, root)) #based on A* evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
                frontier.put((evaluation[1], counter, child)) #based on A* evaluation
    return
