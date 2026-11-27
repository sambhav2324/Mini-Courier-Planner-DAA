# Mini-Courier Planner (DAA Capstone)

Python prototype for K.R. Mangalam University's Design & Analysis of Algorithms capstone. It combines parcel priority sorting, 0/1 Knapsack packing, Dijkstra shortest paths and Nearest-Neighbor TSP route approximation, plus sorting runtime experiments.

## Requirements
- Python 3.9+ (core app and tests use only the standard library)
- Optional: `matplotlib` for the benchmark PNG chart

## Run on Windows
1. Extract the ZIP.
2. Open the extracted `MiniCourierPlanner` folder in VS Code.
3. Open Terminal (PowerShell) in that folder.
4. Run:
   ```powershell
   python main.py
   ```
5. Change the packing capacity:
   ```powershell
   python main.py --capacity 25
   ```
6. Run benchmark and create CSV + chart:
   ```powershell
   python main.py --benchmark
   ```
   For a chart, install optional package first: `python -m pip install matplotlib`.
7. Run automated tests:
   ```powershell
   python -m unittest discover -s tests -v
   ```

## Use a custom dataset
Pass a JSON path: `python main.py --data data/sample_city.json --capacity 30`. The JSON has a `depot`, a weighted adjacency-list `graph`, and `parcels`. Each parcel includes `id`, `destination`, `priority`, `deadline`, `weight`, and `value`. Edge weights must be non-negative. Use the same node names in graph and parcel destinations.

## How the algorithms work
- **Merge Sort:** sorts by priority descending, deadline ascending, ID ascending. Time O(n log n), auxiliary space O(n).
- **Quick Sort:** independently sorts with median-of-three pivot; used to verify the Merge Sort result and benchmark. Average O(n log n), worst O(n²); recursion space depends on partition balance.
- **0/1 Knapsack DP:** chooses the parcel subset maximizing total value under bag capacity. Time O(nW), space O(nW), where W is capacity.
- **Dijkstra:** finds shortest paths on nonnegative weighted graph using a heap. Typical O((V+E) log V).
- **Nearest Neighbor TSP approximation:** starts at depot, repeatedly visits the closest unvisited selected destination by shortest-path distance, and returns to depot when reachable. It is a heuristic, not guaranteed optimal.

## Project layout
- `main.py` — command-line entry point
- `src/algorithms.py` — algorithm implementations
- `src/planner.py` — integration, output and benchmark
- `data/sample_city.json` — ready-to-run example
- `tests/test_algorithms.py` — unit tests
- `docs/REPORT.md` — report draft for submission
- `results/` — generated benchmark outputs


