# mdp_solver/value_iteration.py


def value_iteration(states, actions, transition_probs, rewards, gamma=0.9, max_iter=1000):
    """
    Implements the Value Iteration algorithm for MDPs.
    
    This version runs for a fixed number of iterations (max_iter).
    
    Parameters:
        states: list of states
        actions: list of actions
        transition_probs: dict, where for each state s and action a, 
                          transition_probs[s][a] is a dict mapping s' to probability.
        rewards: dict, where rewards[(s, a)] gives the immediate reward for taking action a in state s.
        gamma: discount factor
        max_iter: maximum number of iterations to run the algorithm
        
    Returns:
        policy: dict mapping each state to the best action
        V: dict mapping each state to its computed value
    """
    # Initialize value function arbitrarily (here, all zeros)
    V = {s: 0 for s in states}
    
    # Iterate a fixed number of times
    for iteration in range(max_iter):
        V_new = {}
        for s in states:
            # Compute Q-value for each action for state s
            q_values = []
            for a in actions:
                # Calculate Q(s, a) = reward + gamma * expected future value
                q_value = rewards.get((s, a), 0) + gamma * sum(
                    transition_probs.get(s, {}).get(a, {}).get(s_prime, 0) * V[s_prime]
                    for s_prime in states
                )
                q_values.append(q_value)
            # The new value for state s is the maximum Q-value across all actions
            V_new[s] = max(q_values)
        V = V_new  # Update V after each iteration
    
    # Extract the policy using the final value function
    policy = {}
    for s in states:
        best_action = max(
            actions,
            key=lambda a: rewards.get((s, a), 0) + gamma * sum(
                transition_probs.get(s, {}).get(a, {}).get(s_prime, 0) * V[s_prime]
                for s_prime in states
            )
        )
        policy[s] = best_action
    
    return policy, V
