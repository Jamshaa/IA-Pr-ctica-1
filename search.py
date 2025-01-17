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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))


    Important note: All of your search functions need to return a list of actions that will lead the agent from the start to the goal. 
                    These actions all have to be legal moves (valid directions, no moving through walls).

    Important note: Make sure to use the Stack, Queue and PriorityQueue data structures provided to you in util.py! 
                    These data structure implementations have particular properties which are required for compatibility with the autograder.

    """
    "*** YOUR CODE HERE ***"
    

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    directions = []
    visited_states = []

    #Add start
    get_start = problem.getStartState()
    fringe.push( (get_start, []) )
    visited_states.append(get_start)

    while not fringe.isEmpty():
        
        get_state_xy, directions = fringe.pop()

        if problem.isGoalState(get_state_xy):
            return directions

        else:
            for successor, direction, cost in problem.getSuccessors(get_state_xy):
                # Track visited states
                if not successor in visited_states:
                    visited_states.append(successor)
                    fringe.push((successor, directions + [direction]))
                    #print(directions)        
    return []
    util.raiseNotDefined()
def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    start_node = problem.getStartState()
    start_heuristic = heuristic(start_node, problem)
    visited_nodes = []
    fringe.push( (start_node, [], 0), start_heuristic)
    directions = []
    while not fringe.isEmpty():
        get_xy, directions, get_cost = fringe.pop()

        if problem.isGoalState(get_xy):
            return directions
        
        if not get_xy in visited_nodes:
            # Track visited_nodes
            visited_nodes.append(get_xy)
            
            for coordinates, direction, successor_cost in problem.getSuccessors(get_xy):
                if not coordinates in visited_nodes:
                    # Pass by reference
                    actions_list = list(directions)
                    actions_list += [direction]
                    # Get cost so far
                    cost_actions = problem.getCostOfActions(actions_list)
                    get_heuristic = heuristic(coordinates, problem)
                    fringe.push( (coordinates, actions_list, 1), cost_actions + get_heuristic)
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
