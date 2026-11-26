from algorithms.merge_sort import merge_sort_products
from algorithms.knapsack import choose_products
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor_tsp
from utils import load_json, money


def show_products(products):
    print("\nPRODUCT PRIORITIZATION")
    print("-" * 76)
    print(f"{'ID':<7}{'Product':<20}{'Price':>10}{'Priority':>12}{'Utility':>10}{'Store':>12}")
    for p in products:
        print(f"{p['id']:<7}{p['name']:<20}{money(p['price']):>10}{p['priority']:>12}{p['utility']:>10}{p['store']:>12}")


def main():
    products = load_json("data/products.json")
    graph = load_json("data/store_graph.json")
    capacity = 5000

    print("=" * 62)
    print("       SMART SHOPPING BUDGET PLANNER")
    print("=" * 62)
    raw = input(f"Enter your shopping budget in rupees [default {capacity}]: ").strip()
    if raw:
        try:
            capacity = int(raw)
            if capacity < 0:
                raise ValueError
        except ValueError:
            print("Invalid budget. Using default budget of Rs.", capacity)

    ordered = merge_sort_products(products)
    show_products(ordered)

    selected, total_cost, total_utility = choose_products(ordered, capacity)
    print("\nOPTIMAL SHOPPING BASKET (0/1 KNAPSACK)")
    print("-" * 50)
    if selected:
        for p in selected:
            print(f"- {p['name']}: {money(p['price'])} | utility {p['utility']}")
    else:
        print("No products fit within the budget.")
    print(f"Total cost: {money(total_cost)}")
    print(f"Total utility: {total_utility}")
    print(f"Remaining budget: {money(capacity - total_cost)}")

    # Plan a route through the stores represented in the selected basket.
    stores = list(dict.fromkeys(p["store"] for p in selected))
    if stores:
        print("\nSTORE-TO-STORE SHORTEST PATHS (DIJKSTRA)")
        for store in stores:
            distance, path = dijkstra(graph, "Home", store)
            print(f"Home -> {store}: {distance} km | path: {' -> '.join(path) if path else 'unreachable'}")

        print("\nSHOPPING VISIT ORDER (NEAREST-NEIGHBOR TSP APPROXIMATION)")
        route, route_distance = nearest_neighbor_tsp(graph, "Home", stores, return_to_start=True)
        print(" -> ".join(route))
        print(f"Approximate route distance: {route_distance} km")
    else:
        print("\nNo store visit is required because no products were selected.")

    print("\nPlanning complete. See README.md for algorithm details and test instructions.")


if __name__ == "__main__":
    main()
