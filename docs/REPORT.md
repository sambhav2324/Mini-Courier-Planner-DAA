# Mini-Courier Planner — Capstone Report

**Course:** Design & Analysis of Algorithms (ETCCDA302)  
**University:** K.R. Mangalam University, Gurugram  
**Student:** ____________________  **Roll No.:** ____________________  
**Faculty:** Dr. Shweta Agarwal

## 1. Problem and Objective
A courier has a depot, delivery locations connected by roads with non-negative distances, and parcels with priority, deadline, weight, and value. The system should prioritize parcels, choose a high-value feasible load for a single trip, and plan a route to visit the chosen destinations and return to the depot when possible.

## 2. Data Design
The graph is represented by an adjacency list: each node maps to connected nodes and edge distances. The sample uses `DEPOT` and locations A–E. Parcel records include a unique ID, destination, priority (higher is more urgent), deadline (smaller is earlier), weight, and value. The bag capacity is configurable from the command line.

## 3. Algorithms and Integration
1. **Merge Sort** orders parcels by descending priority, then ascending deadline, then parcel ID. This produces a predictable urgency order.
2. **Quick Sort** independently sorts the same parcel list. The program checks that both outputs match, and the sorting benchmark compares their runtimes with Python's built-in sort.
3. **0/1 Knapsack Dynamic Programming** chooses the subset with maximum total value subject to the capacity. Each parcel is either selected once or not selected. The program reconstructs the selected parcel list from the DP table.
4. **Dijkstra's Algorithm** is run from the depot and each selected destination to obtain pairwise shortest-path distances and path sequences.
5. **Nearest-Neighbor TSP Approximation** starts at the depot and chooses the closest unvisited selected destination at each step. It then adds a return-to-depot leg if reachable. This is a practical route heuristic; it does not claim to find an optimal TSP tour.

## 4. Complexity Analysis
Let n be parcels, W be capacity, V be graph vertices, E be edges, and k be selected unique delivery locations. Merge Sort is O(n log n) time and O(n) extra space. Average Quick Sort is O(n log n), worst O(n²). Knapsack DP is O(nW) time and O(nW) memory. Heap-based Dijkstra is O((V+E) log V) per source; it is run for depot plus k destinations. Nearest Neighbor is O(k²) over the distance table. The expanded road path uses shortest paths for each route leg.

## 5. Testing
The project includes unit tests for sorting consistency/order, Knapsack, Dijkstra and route approximation. The sample dataset includes eight parcels, a six-node weighted graph and default bag capacity 30. Run tests with `python -m unittest discover -s tests -v`. Run the system with `python main.py`. Performance tests use synthetic parcel counts 50, 150, 300 and 600 and export measurements to CSV. A chart is generated if Matplotlib is installed.

## 6. Results
Run the program locally and paste the actual terminal output here. Record actual benchmark values from `results/sorting_benchmark.csv` and insert the generated `sorting_runtime.png` chart. Runtime is machine-dependent, so do not use benchmark numbers from another device.

## 7. Limitations and Future Work
The route method is an approximation; an exact TSP solver is expensive as destinations grow. The packing objective currently maximizes parcel value and does not include travel cost, deadline feasibility, or delivery-time windows. Future improvements could add time-window constraints, multiple couriers, traffic/time-dependent edges, a stronger TSP heuristic (2-opt), and scalable knapsack approximations.

## 8. Conclusion
The prototype demonstrates how sorting, dynamic programming, graph shortest paths and approximation can be combined into a courier planning workflow. It exposes the selected load, route, distance and runtime measurements, and provides testable modular implementations.

## Evidence checklist
- [ ] Screenshot of the normal application report
- [ ] Screenshot of benchmark run
- [ ] Runtime CSV and chart
- [ ] Unit-test success output
- [ ] Fill in student name and roll number
