class Item:
    def __init__(self, item_weight, item_value):
        self.weight = item_weight
        self.value = item_value
        self.fraction = 1.0


class Knapsack:
    def __init__(self, weight, items):
        self.max_weight = weight
        self.item_list = items


def value_to_weight_ratio(item):
    return item.value / item.weight

def fractional_knapsack(knapsack, item_list):
    item_list.sort(key = value_to_weight_ratio, reverse=True)
    remaining = knapsack.max_weight
    for item in item_list:
        if item.weight <= remaining:
            knapsack.item_list.append(item)
            remaining = remaining - item.weight
        else:
            item.fraction = remaining / item.weight
            knapsack.item_list.append(item)
            break

