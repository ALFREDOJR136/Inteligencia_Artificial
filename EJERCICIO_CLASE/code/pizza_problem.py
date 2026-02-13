from problems import Problem 

class Pizza(Problem):
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        valid_actions=[]
        