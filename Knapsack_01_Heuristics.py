from operator import attrgetter


class Item:
    def __init__(self, item_weight, item_value):
        self.weight = item_weight
        self.value = item_value


class Knapsack:
    def __init__(self, weight, items):
        self.max_weight = weight
        self.item_list = items


def knapsack_01(knapsack, item_list):
    item_list.sort(key = attrgetter("value"), reverse=True)
    remaining = knapsack.max_weight
    for item in item_list:
        if item.weight <= remaining:
            knapsack.item_list.append(item)
            remaining = remaining - item.weight

