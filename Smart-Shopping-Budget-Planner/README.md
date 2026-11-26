# Smart Shopping Budget Planner
**DAA Capstone Project | Python**

A console-based prototype that prioritizes products, selects a high-utility basket within a fixed budget, computes shortest paths between stores, and creates an approximate store-visiting tour.

## Features
- Merge Sort: sorts products by priority (descending), deadline (ascending), price (ascending), then ID.
- 0/1 Knapsack DP: maximizes total utility without exceeding the user's rupee budget.
- Dijkstra: computes shortest paths over a weighted store graph.
- Nearest Neighbor TSP: approximates a round trip visiting the stores represented in the selected basket.
- Performance benchmark: writes CSV results and, when Matplotlib is installed, a runtime chart.
- Unit tests for the core algorithms.

## Requirements
- Python 3.9 or newer
- Matplotlib is optional (only needed for the runtime chart)

## Run on Windows PowerShell
```powershell
cd "path\to\Smart-Shopping-Budget-Planner"
python main.py
```
Enter a budget in whole rupees when prompted. Press Enter to use the sample budget of Rs. 5,000.

Run tests:
```powershell
python -m unittest discover -s tests -v
```

Run performance tests:
```powershell
python -m pip install -r requirements.txt
python reports/performance.py
```
The benchmark creates `reports/runtime_results.csv` and `reports/runtime_chart.png`.

## Project structure
```text
Smart-Shopping-Budget-Planner/
├── main.py
├── utils.py
├── algorithms/
│   ├── merge_sort.py
│   ├── knapsack.py
│   ├── dijkstra.py
│   └── tsp.py
├── data/
│   ├── products.json
│   └── store_graph.json
├── reports/
│   └── performance.py
├── tests/
│   └── test_algorithms.py
├── screenshots/
├── requirements.txt
└── README.md
```

## Sample workflow
1. Enter a budget.
2. Products are sorted by priority and deadline.
3. Knapsack selects the combination with maximum utility within budget.
4. Dijkstra prints shortest paths from Home to each selected store.
5. Nearest Neighbor suggests a round-trip store visit order.
6. Run the benchmark to compare execution times.

## Algorithm notes and complexity
| Component | Purpose | Time complexity |
|---|---|---|
| Merge Sort | Product ordering | O(n log n) |
| 0/1 Knapsack DP | Budget-constrained selection | O(nB), where B is budget in integer rupees |
| Dijkstra with heap | Shortest path | O((V+E) log V) |
| Nearest Neighbor TSP | Approximate visit order | O(k²) distance choices, plus shortest-path computations |

The classic DP implementation uses one column per rupee. For very large budgets, consider scaling prices to a suitable unit (for example, paise-to-rupee or 10-rupee units) while documenting the resulting precision trade-off.

## Data format
`data/products.json` contains `id`, `name`, `price`, `priority`, `utility`, `deadline`, and `store`.
`data/store_graph.json` is an undirected weighted adjacency-list graph. Every road should be represented in both directions with the same distance.

## DAA capstone phase mapping
1. **Problem design and planning:** parcel/product attributes, budget, store graph and algorithm plan.
2. **Prioritization and box filling:** Merge Sort + 0/1 Knapsack; selected products and totals.
3. **Graph processing:** Dijkstra shortest paths + Nearest Neighbor TSP route.
4. **Performance testing:** run `reports/performance.py`; preserve CSV/chart and discuss trends.
5. **Final report and demonstration:** use this README, add your own screenshots, test results and viva explanation.

## Important limitations
- This is an academic prototype, not a live shopping or payment application.
- Product prices, utilities, stores and distances are sample data in JSON files.
- Utility values are illustrative scores entered in the dataset, not AI-generated recommendations.
- TSP nearest-neighbor is an approximation and does not guarantee the globally shortest tour.
- The route is calculated over the sample store graph; it does not use live maps or traffic.

## Suggested evidence to add before submission
- Screenshot of the program run with a chosen budget.
- Screenshot of the product JSON and store graph.
- Test output from `python -m unittest discover -s tests -v`.
- `runtime_results.csv` and `runtime_chart.png`.
- A short report explaining test datasets, observed results and future improvements.
