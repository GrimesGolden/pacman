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
    from util import Stack  # Stack ensures LIFO (last-in, first-out) behavior

    my_stack = Stack()  # Stack stores (state, path)
    visited = set()  # Tracks visited states

    my_stack.push((problem.getStartState(), []))  # Start state with an empty path

    while not my_stack.isEmpty():
        xy, path = my_stack.pop()  # Pop the most recent state

        if problem.isGoalState(xy):  # Goal check
            return path

        if xy not in visited:
            visited.add(xy)  # Mark as visited
            for nextState, action, _ in problem.getSuccessors(xy): # Recall successors returns both state (coordinates), and actions (path)
                if nextState not in visited:
                    my_stack.push((nextState, path + [action]))  # Add new path to stack

    return []  # Return empty if no solution found

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue # we need Queue for breadth first (FIFO)

    # Queue format ((x,y),[path to this coordinate]) #
    my_q = Queue()

    visited = set()  # Tracks visited states
    path = [] # Each state knows the path to its coordinate

     # Check if initial state is the end goal.
    # Simply return an empty list in this case, state is already valid. 
    if problem.isGoalState(problem.getStartState()):
        return []

    # Push initial state, the initial path is an empty list #
    my_q.push((problem.getStartState(),[]))

    while not my_q.isEmpty():
        xy, path = my_q.pop()  # Dequeue the oldest state

        if problem.isGoalState(xy):  # Goal check
            return path

        if xy not in visited:
            visited.add(xy)  # Mark as visited
            for nextState, action, _ in problem.getSuccessors(xy):
                if nextState not in visited:
                    my_q.push((nextState, path + [action]))  # Add new path to queue

    return []  # Return empty if no solution found

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
