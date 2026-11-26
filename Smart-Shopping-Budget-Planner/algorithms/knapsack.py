def choose_products(products, budget):
    budget = int(budget)
    if budget < 0:
        raise ValueError("Budget cannot be negative.")
    n = len(products)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        price = int(products[i - 1]["price"])
        utility = int(products[i - 1]["utility"])
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if price <= b:
                dp[i][b] = max(dp[i][b], utility + dp[i - 1][b - price])

    selected = []
    remaining = budget
    for i in range(n, 0, -1):
        if dp[i][remaining] != dp[i - 1][remaining]:
            product = products[i - 1]
            selected.append(product)
            remaining -= int(product["price"])
    selected.reverse()
    total_cost = sum(int(p["price"]) for p in selected)
    total_utility = sum(int(p["utility"]) for p in selected)
    return selected, total_cost, total_utility


def build_dp_table(products, budget):
    
    n = len(products)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i, p in enumerate(products, 1):
        w, v = int(p["price"]), int(p["utility"])
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if w <= b:
                dp[i][b] = max(dp[i][b], v + dp[i - 1][b - w])
    return dp
