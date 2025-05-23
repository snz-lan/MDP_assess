# MDP Solver - Value Iteration 

## Overview

This project provides a solution to Markov Decision Process (MDP) problems using the value iteration algorithm. It includes an implementation of value iteration algorithm to solve the MDP, along with tests and examples demonstrating how to use the package. The goal is to create an easy-to-use Python package for anyone interested in solving MDP problems.

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
5. [Contributors](#contributors)
6. [How to Cite This Work](#how-to-cite-this-work)


---

## Installation

To install the package, you can either use `pip` from GitHub or install it from the local source.

### From GitHub:
To install the package directly from GitHub, run the following command:

```bash
pip install git+https://github.com/snz-lan/MDP_assess.git
```
## Usage

Once installed, you can import the package and use the algorithms. Below are examples of how to use the **Value Iteration**  algorithm.

### Value Iteration

The value iteration algorithm is used to compute the optimal value function and policy for a given MDP.

#### Example Code:

```python
from mdp_solver.value_iter import value_iteration

# Defining the MDP for Sam's problem
states = ['healthy', 'sick']
actions = ['relax', 'party']

# transition probabilities as given:
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

# imm. rewards as given:
rewards = {
    ('healthy', 'relax'): 7,
    ('healthy', 'party'): 10,
    ('sick', 'relax'): 0,
    ('sick', 'party'): 2
}

# a discount factor gamma = 0.8, as specified in the example.
gamma = 0.8
max_iter = 1000

# Run value iteration
policy, values = value_iteration(states, actions, transition_probs, rewards, gamma=gamma, max_iter=max_iter)

print("Optimal Policy:", policy)
print("Optimal Values:", values)
```
## Tests
The project includes unit tests to verify the correctness of the algorithms. Tests are located in the tests/ directory.

### Running Tests Locally
Navigate to the root directory of the project.

Run the tests using unittest:

```bash
python -m unittest discover mdp_solver/tests
```
You can also run individual test files:

```bash
!python -m mdp_solver.examples
```
The test suite will check if the algorithms behave as expected under different conditions.

## License

Copyright (C) 2025 [Shahnaz Abdul Hameed]

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/gpl-3.0.txt](https://www.gnu.org/licenses/gpl-3.0.txt).

## Contributors

- [Shahnaz Abdul Hameed] – Author, Maintainer  

## How to Cite This Work

If you use this package in your research, please consider citing it as:

```bibtex
@software{mdp_solver_2025,
  author       = {Shahnaz Abdul Hameed},
  title        = {MDP_solver: A Markov Decision Process Solver},
  month        = Mar,
  year         = 2025,
  version      = {v1.0},
  url          = {https://github.com/snz-lan/MDP_assess}
}




