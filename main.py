from searchAlgorithms import *
from state import State
from time import time
from random import *

#count the number of inversions       
def inv_num(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1 , len(puzzle)):
            print("i:%d, j:%d, puzzle[%d]:%d, puzzle[%d]%d, inv:%d" % (i, j, i, puzzle[i], j, puzzle[j], inv))
            if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):

                inv += 1
    return inv

def solvable(puzzle): #check if initial state puzzle is solvable: number of inversions should be even.
    return True
    # inv_counter = inv_num(puzzle)
    # if (inv_counter %2 ==0):
    #     return True
    # return False

def print_puzzle(puzzle):
    tmp_counter = 0
    for num in puzzle:
        if tmp_counter >= n:
            print()
            tmp_counter = 0
            
        if num > 9:
            print(num, end=' | ')
        else:
            print(num, end='  | ')
        tmp_counter = tmp_counter+1
    print()
    
#1,8,2,0,4,3,7,6,5 is solvable
#2,1,3,4,5,6,7,8,0 is not solvable
if __name__ == '__main__':
    # initial state
    # n = int(input("Enter n\n"))
    # print("Enter your" ,n,"*",n, "puzzle")
    # root = []
    # for i in range(0,n*n):
    #     p = int(input())
    #     root.append(p)
    
    # n = 3
    # root = [0,1,2,7,6,4,3,8,5]

    n = 4
    # root = [2,6,7,13,5,4,11,12,1,3,8,10,14,15,9,0]

    #easy version
    root = [2, 3,4,5,
            1,12,14,6,
           11,13,15,7,
           10, 9, 0,8]

    # root = []

    # random initial state generator
    while len(root) < 16:
        rn = randint(0, 15)
        if rn not in root:
            root.append(rn)
            
    # print(gen_root)

    print("Initial state is:")
    print_puzzle(root)
    print("Goal state is:")
    if n == 3:
        State.goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        # State.goal = gen_goal 
    elif n == 4:
        State.goal = [1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7]
    
    print_puzzle(State.goal)
    
    print("Please wait..... \n")
                 
    start_time = time()
    IDS_solution = IDS(root, n)
    IDS_time = time() - start_time
    print('IDS Solution is ', IDS_solution[0])
    print('STEP:', len(IDS_solution[0]))
    print('Number of explored nodes is ', IDS_solution[1])
    print('IDS Time:%.4fms' % (IDS_time*1000), "\n")  
    
    start_time = time()
    UCS_solution = UniformCostSearch(root, n)
    UCS_time = time() - start_time
    print('UCS is ', UCS_solution[0])
    print('STEP:', len(UCS_solution[0]))
    print('Number of explored nodes is ', UCS_solution[1])   
    print('UCS Time:%.4fms' % (UCS_time*1000), "\n")
    
    start_time = time()
    Greedy_solution = Greedy(root, n)
    Greedy_time = time() - start_time
    print('Greedy with Manhattan Distance Solution is ', Greedy_solution[0])
    print('STEP:', len(Greedy_solution[0]))
    print('Number of explored nodes is ', Greedy_solution[1])   
    print('Greedy Time:%.4fms' % (Greedy_time*1000) , "\n")
    
    start_time = time()
    AStar_solution = AStar_search(root, n)
    AStar_time = time() - start_time
    print('A* with Manhattan Distance Solution is ', AStar_solution[0])
    print('STEP:', len(AStar_solution[0]))
    print('Number of explored nodes is ', AStar_solution[1])   
    print('A* Time:%.4fms' % (AStar_time*1000), "\n")
    
    start_time = time()
    RBFS_solution = RBFS(root, n)
    RBFS_time = time() - start_time
    print('RBFS is ', RBFS_solution[0])
    print('STEP:', len(RBFS_solution[0]))
    print('Number of successors is ', RBFS_solution[1])   
    print('RBFS Time:%.4fms' % (RBFS_time*1000), "\n")