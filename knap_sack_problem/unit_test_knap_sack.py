import unittest
from bruteForce_0_1_knapsack import brute_force_knap_sack
from greedy_fractional_knapsack import fractionalKnapsackGreedy, Item
from dynamic_0_1_knapsack import knapSackDynamic


class bruteforce_knapsack_test(unittest.TestCase):

    def test_normal(self):
        item_profit = [60, 100, 20]
        item_weight = [10, 20, 30]
        bag_size = 50
        no_of_items = len(item_profit)
        result = 160

        self.assertEqual(brute_force_knap_sack(bag_size, item_weight, item_profit, no_of_items), result)

    def test_zero_bag_capacity(self):
        item_profit = [60, 100, 20]
        item_weight = [10, 20, 30]
        bag_size = 0
        no_of_items = len(item_profit)
        result = 0

        self.assertEqual(brute_force_knap_sack(bag_size, item_weight, item_profit, no_of_items), result)

    def test_big_item(self):
        item_profit = [60, 100, 20]
        item_weight = [1000, 2000, 3000]
        bag_size = 0
        no_of_items = len(item_profit)
        result = 0

        self.assertEqual(brute_force_knap_sack(bag_size, item_weight, item_profit, no_of_items), result)


class greedy_fractional_knapsack_test(unittest.TestCase):

    def test_normal(self):
        W = 50
        arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
        max_val = fractionalKnapsackGreedy(W, arr)
        result = 240.0

        self.assertEqual(max_val, result)

    def test_zero_bag_capacity(self):
        W = 0
        arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
        max_val = fractionalKnapsackGreedy(W, arr)
        result = 0

        self.assertEqual(max_val, result)

    def test_big_weights(self):
        W = 100
        arr = [Item(60, 1000), Item(100, 200), Item(120, 300)]
        max_val = fractionalKnapsackGreedy(W, arr)
        result = 50.0

        self.assertEqual(max_val, result)


class dynamic_knapsack_test(unittest.TestCase):

    def test_normal(self):
        val = [60, 100, 120]
        wt = [10, 20, 30]
        W = 50
        n = len(val)
        max_val = knapSackDynamic(W, wt, val, n)
        result = 220

        self.assertEqual(max_val, result)

    def test_zero_bag_capacity(self):
        val = [60, 100, 120]
        wt = [10, 20, 30]
        W = 0
        n = len(val)
        max_val = knapSackDynamic(W, wt, val, n)
        result = 0

        self.assertEqual(max_val, result)

    def test_big_weights(self):
        val = [60, 100, 120]
        wt = [1000, 2000, 300]
        W = 50
        n = len(val)
        max_val = knapSackDynamic(W, wt, val, n)
        result = 0

        self.assertEqual(max_val, result)


if __name__ == "__main__":
    unittest.main()