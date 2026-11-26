import csv
import random
import time
from pathlib import Path
from algorithms.merge_sort import merge_sort_products
from algorithms.knapsack import choose_products
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor_tsp

def benchmark():
    rows = []
    graph = {
        "Home":{"A":2,"B":5,"C":7,"D":4},
        "A":{"Home":2,"B":3,"C":4,"D":6},
        "B":{"Home":5,"A":3,"C":2,"D":3},
        "C":{"Home":7,"A":4,"B":2,"D":1},
        "D":{"Home":4,"A":6,"B":3,"C":1}
    }
    for size in (10, 50, 100, 250):
        products = [
            {"id":f"P{i:04}","name":f"Item{i}","price":random.randint(10,100),
             "priority":random.randint(1,5),"utility":random.randint(1,100),
             "deadline":f"2026-12-{random.randint(1,28):02}","store":"A"}
            for i in range(size)
        ]
        start = time.perf_counter()
        merge_sort_products(products)
        sort_ms = (time.perf_counter()-start)*1000

        # Keep budget moderate because classic 0/1 DP is O(n * budget).
        start = time.perf_counter()
        choose_products(products, 1000)
        knapsack_ms = (time.perf_counter()-start)*1000

        start = time.perf_counter()
        dijkstra(graph, "Home", "C")
        dijkstra_ms = (time.perf_counter()-start)*1000

        start = time.perf_counter()
        nearest_neighbor_tsp(graph, "Home", ["A","B","C","D"])
        tsp_ms = (time.perf_counter()-start)*1000

        rows.append({"input_size":size,"merge_sort_ms":sort_ms,
                     "knapsack_ms":knapsack_ms,"dijkstra_ms":dijkstra_ms,
                     "nearest_neighbor_tsp_ms":tsp_ms})

    output = Path(__file__).with_name("runtime_results.csv")
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved benchmark results to {output}")

    try:
        import matplotlib.pyplot as plt
        names = ["merge_sort_ms","knapsack_ms","dijkstra_ms","nearest_neighbor_tsp_ms"]
        for name in names:
            plt.plot([r["input_size"] for r in rows], [r[name] for r in rows], marker="o", label=name)
        plt.xlabel("Number of products (graph size fixed for graph algorithms)")
        plt.ylabel("Runtime (milliseconds)")
        plt.title("Smart Shopping Planner - Runtime Comparison")
        plt.legend()
        plt.grid(True)
        chart = Path(__file__).with_name("runtime_chart.png")
        plt.savefig(chart, dpi=160, bbox_inches="tight")
        plt.close()
        print(f"Saved chart to {chart}")
    except ImportError:
        print("matplotlib is not installed; CSV is available. Install requirements to create chart.")

if __name__ == "__main__":
    benchmark()
