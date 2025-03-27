# MDP Solver - Value Iteration and Policy Iteration

## Overview

This project provides a solution to Markov Decision Process (MDP) problems using the value iteration algorithm. It includes tools to solve the MDP, along with tests and examples demonstrating how to use the package. The goal is to create an easy-to-use Python package for anyone interested in solving MDP problems.

### Features:
- **Value Iteration**: Implementation of the value iteration algorithm to solve MDPs.
- **Testing**: Unit tests for verifying correctness of the algorithms.
- **Examples**: Sample usage of the algorithms in different MDP scenarios.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
   - [Value Iteration](#value-iteration)
3. [Tests](#tests)
4. [License](#license)

---

## Installation

To install the package, you can either use `pip` from GitHub or install it from the local source.

### From GitHub:
To install the package directly from GitHub, run the following command:

```bash
pip install git+https://github.com/snz-lan/MDP_assess.git
```
## Usage

Once installed, you can import the package and use the algorithms. Below are examples of how to use the **Value Iteration** and **Policy Iteration** algorithms.

### Value Iteration

The value iteration algorithm is used to compute the optimal value function and policy for a given MDP.

#### Example Code:

```python
from mdp_solver.value_iter import value_iteration

# Define the MDP parameters (states, actions, transitions, and rewards)
states = ['healthy', 'sick']
actions = ['relax', 'party']
transition_probabilities = {
    'healthy': {'relax': {'healthy': 0.95, 'sick': 0.05}, 'party': {'healthy': 0.7, 'sick': 0.3}},
    'sick': {'relax': {'healthy': 0.5, 'sick': 0.5}, 'party': {'healthy': 0.1, 'sick': 0.9}},
}
rewards = {
    'healthy': {'relax': 7, 'party': 10},
    'sick': {'relax': 0, 'party': 2},
}
gamma = 0.8  # Discount factor

# Call the value iteration function
value_function, policy = value_iteration(states, actions, transition_probabilities, rewards, gamma)

print("Optimal Value Function:", value_function)
print("Optimal Policy:", policy)
```
#### Tests
The project includes unit tests to verify the correctness of the algorithms. Tests are located in the tests/ directory.

### Running Tests Locally
Navigate to the root directory of the project.

Run the tests using unittest:

```bash
python -m unittest discover -s tests
```
You can also run individual test files:

```bash
python -m unittest tests.test_value_iteration
```
The test suite will check if the algorithms behave as expected under various conditions.




