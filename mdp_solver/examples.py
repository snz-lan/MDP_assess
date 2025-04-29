# mdp_solver/examples.py

from mdp_solver.value_iter import value_iteration

def run_sam_example():
    """
    Implements the MDP for Sam's decision-making (Example 9.27).
    
    States:
        'healthy', 'sick'
    Actions:
        'relax', 'party'
    
    Transition probabilities:
        - If healthy and relax: 95% stay healthy.
        - If healthy and party: 70% remain healthy (thus 30% chance to become sick).
        - If sick and relax: 50% chance to become healthy.
        - If sick and party: 10% chance to become healthy.
    
    Rewards:
        - (healthy, relax): 7
        - (healthy, party): 10
        - (sick, relax): 0
        - (sick, party): 2
    """
    # Defining the states and actions
    states = ['healthy', 'sick']
    actions = ['relax', 'party']
    
    # this is the transition prob. dictionary
    transition_probs = {
        'healthy': {
            'relax': {'healthy': 0.95, 'sick': 0.05},
            'party': {'healthy': 0.7, 'sick': 0.3}
        },
        'sick': {
            'relax': {'healthy': 0.5, 'sick': 0.5},
            'party': {'healthy': 0.1, 'sick': 0.9}
        }
    }
    
    # Reward dictionary
    rewards = {
        ('healthy', 'relax'): 7,
        ('healthy', 'party'): 10,
        ('sick', 'relax'): 0,
        ('sick', 'party'): 2
    }
    
    # Running value iteration on Sam's MDP
    policy, values = value_iteration(states, actions, transition_probs, rewards, gamma=0.9, max_iter=1000)
    print("Sam's Optimal Policy:", policy)
    print("Sam's Value Function:", values)

if __name__ == '__main__':
    run_sam_example()

def change(m):
    print("this is a new change")
