def knapsack_dynamic_programming(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, 0, -1):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

# Example usage:
weights = [2, 2, 3, 4, 5]
values = [3, 4, 5, 8, 10]
capacity = 9

max_value = knapsack_dynamic_programming(weights, values, capacity)
print("Maximum value:", max_value)


# o/p   :- Maximum value: 18