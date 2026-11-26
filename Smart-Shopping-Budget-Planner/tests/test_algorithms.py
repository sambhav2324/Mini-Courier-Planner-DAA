import unittest
from algorithms.merge_sort import merge_sort_products
from algorithms.knapsack import choose_products
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor_tsp

class AlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.products = [
            {"id":"P1","name":"A","price":4,"priority":2,"utility":8,"deadline":"2026-11-20","store":"A"},
            {"id":"P2","name":"B","price":5,"priority":1,"utility":9,"deadline":"2026-11-21","store":"B"},
            {"id":"P3","name":"C","price":3,"priority":3,"utility":6,"deadline":"2026-11-19","store":"C"}
        ]
        self.graph = {"Home":{"A":2,"B":5},"A":{"Home":2,"B":1},"B":{"Home":5,"A":1}}

    def test_sort(self):
        result = merge_sort_products(self.products)
        self.assertEqual([p["id"] for p in result], ["P3","P1","P2"])

    def test_knapsack(self):
        selected, cost, utility = choose_products(self.products, 7)
        self.assertEqual(cost, 7)
        self.assertEqual(utility, 14)

    def test_dijkstra(self):
        distance, path = dijkstra(self.graph, "Home", "B")
        self.assertEqual(distance, 3)
        self.assertEqual(path, ["Home","A","B"])

    def test_tsp(self):
        route, distance = nearest_neighbor_tsp(self.graph, "Home", ["A","B"])
        self.assertEqual(route[0], "Home")
        self.assertEqual(route[-1], "Home")
        self.assertEqual(distance, 6)

if __name__ == "__main__":
    unittest.main()
