# Production Optimization Project
Innovative MPS models and heuristics leveraging Xpress Mosel for effective production optimization, addressing complex scheduling and resource allocation.
---

## Description
This project is a culmination of university group work aimed at optimizing monthly production planning for a machinery line, with a focus on minimizing deviations from the average production pace for each machine type. We developed innovative algorithms to tackle a real-world problem presented by a local company, addressing both resource availability and production constraints.

## Repository Structure
The repository contains several `mosel` scripts used to implement various heuristic and metaheuristic approaches for problem-solving:

- `DatiCreator.py`: Generates data instances for simulations.
- `Euristico Greedy 1.mos`: Implements the first greedy heuristic algorithm.
- `Euristico Greedy Pesato.mos`: A weighted greedy heuristic variant.
- `Iterated Local Search.mos`: Applies iterated local search for improved solutions.
- `Iterated Local Swap.mos`: An iterated local search variation using swap operations.
- `Modello Tesina.mos`: Contains the optimization mathematical model for exact solutions.
- `Multistart Casuale + Localsearch 1.mos`: Combines a random multi-start approach with local search.
- `Multistart Casuale + Swap.mos`: A multi-start variant using swap operations.
- `Multistart Guidato + Localsearch 1.mos`: Guided multi-start with local search.
- `Multistart Guidato + Swap.mos`: Guided multi-start with swap operations.
- `Simulated Annealing.mos`: Implements the simulated annealing algorithm for optimization.

## Usage
To run the scripts, Xpress Mosel is required as the execution environment. Each script can be executed individually to analyze different heuristic and metaheuristic strategies in problem-solving.

