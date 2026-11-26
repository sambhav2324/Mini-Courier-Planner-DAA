# Smart Shopping Budget Planner – Project Report Template

## 1. Introduction
The Smart Shopping Budget Planner is a Python prototype that helps a user select a useful set of products within a fixed spending limit and plan visits to the stores selling those products.

## 2. Problem Statement
Shoppers may have a fixed budget and need to compare multiple products and stores. Selecting products manually can exceed the budget or overlook combinations that provide greater value. Visiting stores in an inefficient order can also increase travel distance.

## 3. Objectives
- Prioritize products using a deterministic sorting rule.
- Maximize total product utility within a fixed budget.
- Calculate shortest paths between store locations.
- Produce an approximate multi-store visit route.
- Measure the runtime of the main algorithmic components.

## 4. Data Design
Describe each product field: product ID, name, price in whole rupees, priority, utility, deadline and store. Describe the store graph as a weighted adjacency list where edge weights represent distances in kilometres.

## 5. Algorithms and Methodology
### 5.1 Merge Sort
Explain the comparison key: priority descending, deadline ascending, price ascending and product ID ascending. State O(n log n) time complexity.

### 5.2 0/1 Knapsack using Dynamic Programming
Define price as weight, utility as value and shopping budget as capacity. Explain the recurrence:
`DP[i][b] = max(DP[i-1][b], utility[i] + DP[i-1][b-price[i]])` when the product fits; otherwise use `DP[i-1][b]`.
State O(nB) time and O(nB) space for this table implementation.

### 5.3 Dijkstra's Algorithm
Explain the weighted graph, non-negative edge requirement, priority queue and path reconstruction. State O((V+E) log V) with a binary heap.

### 5.4 Nearest Neighbor TSP Approximation
Explain how the algorithm repeatedly chooses the nearest unvisited store and optionally returns to the start. Clarify that it is an approximation and not guaranteed optimal.

## 6. Implementation
Describe the Python modules and how `main.py` integrates them. Include screenshots of your own program execution.

## 7. Testing and Results
Run the supplied unit tests and performance benchmark. Insert your actual test results, runtime CSV values and chart here. Do not invent measured results.

## 8. Discussion
Discuss correctness, the effect of larger product counts and budget values, and why TSP approximation is used instead of exhaustive search.

## 9. Limitations and Future Scope
Possible extensions include live product prices, store APIs, map services, discount rules, user profiles, a graphical interface and persistent storage.

## 10. Conclusion
Summarize how sorting, dynamic programming, shortest-path computation and route approximation work together in the shopping planner.
