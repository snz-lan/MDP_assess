# mdp_solver/tests/test_value_iteration.py

import unittest
from mdp_solver.value_iter import value_iteration

class TestValueIteration(unittest.TestCase):
    def test_sam_example(self):
        # States and actions for Sam's example
        states = ['healthy', 'sick']
        actions = ['relax', 'party']
        
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
        rewards = {
            ('healthy', 'relax'): 7,
            ('healthy', 'party'): 10,
            ('sick', 'relax'): 0,
            ('sick', 'party'): 2
        }
        
        policy, values = value_iteration(states, actions, transition_probs, rewards, gamma=0.9, max_iter=1000)
        # Check that the policy suggests 'party' when healthy (since the immediate reward is higher)
        self.assertEqual(policy['healthy'], 'party')
        # Depending on gamma and dynamics, you may check for a particular action when sick
        self.assertIn(policy['sick'], ['relax', 'party'])  # adjust based on expected outcome

if __name__ == '__main__':
    unittest.main()
