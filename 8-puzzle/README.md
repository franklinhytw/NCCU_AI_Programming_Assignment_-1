# 8-Puzzle-solver-program-assignment

## Input

First n should be entered and then the initial state of puzzle would be a list of numbers from 0 to (n*n)-1. An example of 8-puzzle with n = 3 is:

```
 initial_state = [1, 8, 2, 0, 4, 3, 7, 6, 5]
 ```
 
 Note that if you want to work with n > 3, goal should be changed in State class.
 
## Output
 
 Output of each search algorithm will be the puzzle solution, number of explored nodes and spent time for search.
 
 ```
BFS Solution is  ['Right', 'Up', 'Right', 'Down', 'Down', 'Left', 'Up', 'Right', 'Down']
Number of explored nodes is  224
BFS Time: 0.005887031555175781
```

## Requirement
* (a) Iterative-Deepening Search (IDS)
* (b) Uniform-Cost Search
* (c) Greedy Best-First Search
* (d) A* search
* (e) Recursive Best-First Search (RBFS)

## Reference
https://tristanpenman.com/demos/n-puzzle
https://github.com/aimacode/aima-pseudocode