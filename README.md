# PAI Programs

A comprehensive collection of fundamental Artificial Intelligence algorithms and problem-solving implementations in Python, designed with a focus on object-oriented programming principles and clean code architecture.

## Overview

This repository serves as an educational resource containing classic AI algorithms and search techniques. Each implementation emphasizes clarity, maintainability, and adherence to OOP best practices, making it suitable for students and practitioners looking to understand core AI concepts.

## Repository Contents

The repository includes implementations of the following algorithms and problem solvers:

### Search Algorithms

**A* Search (asearch.py)**  
Implementation of the A* pathfinding algorithm, which combines the benefits of Dijkstra's algorithm and Greedy Best-First Search by using both the actual cost from the start node and a heuristic estimate to the goal.

**AO* Search (aosearch.py)**  
An AND-OR graph search algorithm designed for solving problems that can be decomposed into subproblems, particularly useful in game theory and planning scenarios.

**Greedy Best-First Search (gbfs.py)**  
A heuristic-based search algorithm that expands nodes based on their estimated distance to the goal, prioritizing paths that appear to lead most directly to the solution.

### Logic and Reasoning

**Forward Chaining (chaining.py)**  
An inference method for rule-based systems that starts with known facts and applies inference rules to derive new conclusions, working from premises to conclusions.

**First-Order Predicate Logic (fopl.py)**  
Implementation of logical reasoning using predicates, quantifiers, and variables to represent and manipulate knowledge in a formal logical framework.

### Classic AI Problems

**N-Queens Problem (queen.py)**  
A constraint satisfaction problem solver that places N chess queens on an N×N chessboard such that no two queens threaten each other.

**Traveling Salesman Problem (tsp.py)**  
An optimization algorithm that finds the shortest possible route visiting a set of cities exactly once and returning to the origin city.

**Water Jug Problem (water_jug.py)**  
A state-space search implementation that solves the classic puzzle of measuring exact quantities of water using containers of different capacities.

**Tic-Tac-Toe (tictactoe.py)**  
A game-playing AI implementation, likely using minimax or similar algorithms to make optimal moves in the classic two-player game.

## Technical Approach

The implementations in this repository follow these design principles:

1. **Object-Oriented Design**: Each algorithm is structured using classes and objects, promoting code reusability and modularity.

2. **Clean Code Standards**: Readable variable names, appropriate comments, and logical code organization make the implementations accessible for learning purposes.

3. **Educational Focus**: Code is written to be instructive, with clear logic flow that helps understand the underlying algorithmic concepts.

## Getting Started

### Prerequisites

Python 3.x is required to run these programs. No external dependencies are needed as implementations use standard Python libraries.

### Installation

Clone the repository to your local machine:

```
git clone https://github.com/chetx27/pai-programs.git
cd pai-programs
```

### Usage

Each Python file can be executed independently. Run any program using:

```
python <filename>.py
```

For example:
```
python asearch.py
python queen.py
```

Modify the input parameters within each file as needed to test different scenarios and problem instances.

## Learning Path

For those new to AI algorithms, the following sequence is recommended:

1. Start with search algorithms: Greedy Best-First Search, then A* Search
2. Explore classic problems: N-Queens, Water Jug
3. Study optimization: Traveling Salesman Problem
4. Advance to logic: Forward Chaining, First-Order Predicate Logic
5. Examine complex search: AO* Search

## Contributing

Contributions are welcome. Please ensure any additions maintain the repository's focus on educational clarity and OOP principles. When submitting pull requests, include clear documentation and follow the existing code style.

## License

Please refer to the repository for license information.

## Author

Maintained by [chetx27](https://github.com/chetx27)

## Acknowledgments

This repository is intended for educational purposes, implementing well-known algorithms from the field of Artificial Intelligence. The implementations are based on standard algorithmic approaches documented in AI literature and coursework.
