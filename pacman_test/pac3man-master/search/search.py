# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack 

    my_stack = Stack() # stack holds a (xy, [path])
    nodes_visited = [] # to mark our visited nodes

    if(problem.isGoalState(problem.getStartState())):
        # If were at the goal, simple, we are done. 
        return []
    
    my_stack.push((problem.getStartState(), [])) # Push the initial state (starting position), to the stack 

    while not my_stack.isEmpty():
        node = my_stack.pop() # Remove the top element from the stack
        xy = node[0] # Get its coordinate
        action = node[1] # Initialize the action to get there (all the movements that get us to that node)

        if xy not in nodes_visited:
            nodes_visited.append(xy) # Mark its coordinate as visited

        if(problem.isGoalState(xy)): # If we are at the goal, then return the action which would get us to this node. 
            return action

        for location, move, _ in problem.getSuccessors(xy): # If not at the goal, then look through the successor nodes
            if location not in nodes_visited: # If it is an unvisited node
                node_path = action + [move] # Get to it, which consists of the previous action to the successor node + the subsequent move which brought us here. 
                my_stack.push((location, node_path)) # Push it to the stack
    
    return [] # fail

    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue 
    
    my_queue = Queue() # stack holds a (xy, [path])
    nodes_visited = [] # to mark our visited nodes

    if(problem.isGoalState(problem.getStartState())):
        # If were at the goal, simple, we are done. 
        return [] 
    
    my_queue.push((problem.getStartState(), [])) # Push the initial state (starting position), to the stack 

    while not my_queue.isEmpty():
        node = my_queue.pop() # Remove the top element from the stack
        xy = node[0] # Get its coordinate
        action = node[1] # Initialize the action to get there (all the movements that get us to that node)
     
        if xy not in nodes_visited:
            nodes_visited.append(xy) # Mark its coordinate as visited

        if(problem.isGoalState(xy)): # If we are at the goal, then return the action which would get us to this node. 
            return action

        for location, move, _ in problem.getSuccessors(xy): # If not at the goal, then look through the successor nodes
            if location not in nodes_visited: # If it is an unvisited node
                node_path = action + [move] # Get to it, which consists of the previous action to the successor node + the subsequent move which brought us here. 
                my_queue.push((location, node_path)) # Push it to the stack
                nodes_visited.append(location) # Mark the node as visited, this is a key difference in BFS, there may be multiple routes to deeper nodes from the same layer. This prevents repetition 
    
    return [] # fail

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue

    my_queue = PriorityQueue() # This time, stack holds a (xy, [path]), cost), priority) where priority is the cost
    nodes_visited = {} # to mark our visited nodes, though it's a set now instead of a list, because we also need to hold cost. 

    if(problem.isGoalState(problem.getStartState())):
        # If were at the goal, simple, we are done. 
        return [] 
    
    my_queue.push((problem.getStartState(), [], 0), 0) # Push the initial state (starting position), to the stack 

    while not my_queue.isEmpty():
        node = my_queue.pop()  # ((xy,action,cost),priority)
        xy = node[0]
        action = node[1]
        cost = node[2]
       

        if(problem.isGoalState(xy)): # If we are at the goal, then return the action which would get us to this node. 
            return action

        if xy not in nodes_visited or cost < nodes_visited[xy]: # This time check if the node we are about to expand is visited, OR update it if cheaper. 
            nodes_visited[xy] = cost #Update or intialize cost 
            for location, move, move_cost in problem.getSuccessors(xy): # Only now do we loop through the successors
                my_queue.push((location, action + [move], cost+move_cost), cost+move_cost)
              
    return [] # fail

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    def getHeuristic(state):
        # Used for priority queue with functiom
        # Given a possible state (a node), determines the f(n) = g(n) + h(n) cost of the path. 
        # Yo dog, we heard you like functions, so we put a function in your function, so now you can function while you function. 
        cost = state[2]   # Needs to obtain the cost of the state
        xy = state[0]
        # Also needs to obtain the heuristic of the state
        # Return sum of both
        h_cost = heuristic(xy, problem) # heuristic always takes a (xy coordinate, goal to reach from this coordinate)
        return (cost + h_cost) # returns f(n) = g(n) + h(n)
        


    # Actual code starts here
    from util import PriorityQueueWithFunction

    my_queue = PriorityQueueWithFunction(getHeuristic) # This time, stack holds a (xy, [path]), cost), getHeuristic) 
    # getHeuristic will take the entire (xy, [path], cost) tuple as its argument
    nodes_visited = {} # to mark our visited nodes, though it's a dictionary now instead of a list, because we also need to hold cost. 

    if(problem.isGoalState(problem.getStartState())):
        # If were at the goal, simple, we are done. 
        return [] 
    
    my_queue.push((problem.getStartState(), [], 0)) # Push the initial state (starting position), to the stack 

    while not my_queue.isEmpty():
        node = my_queue.pop()  # ((xy,action,cost),priority)
        xy = node[0]
        action = node[1]
        cost = node[2]
       

        if(problem.isGoalState(xy)): # If we are at the goal, then return the action which would get us to this node. 
            return action

        if xy not in nodes_visited or cost < nodes_visited[xy]: # This time check if the node we are about to expand is visited, OR update it if cheaper. 
            nodes_visited[xy] = cost #Update or intialize cost 
            for location, move, move_cost in problem.getSuccessors(xy): # Only now do we loop through the successors
                my_queue.push((location, action + [move], cost+move_cost)) # Note: we don't need priority this time, the getHeuristic calculates the priority as f(n) for us. 
              
    return [] # fail

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
