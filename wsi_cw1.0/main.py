def allCombinations(itterable):
    n = len(itterable)
    if n < 1:
        return None
    if n == 1:
        return [[], [itterable[0]]]
    comb_list1 = allCombinations(itterable[1:])
    comb_list2 = comb_list1.copy()
    for elem in comb_list1:
        new_elem = elem.copy()
        new_elem.append(itterable[0])
        comb_list2.append(new_elem)
    return comb_list2


def bruteForceAlgorithm(item_list, max_weight):
    all_comb = allCombinations(item_list)
    best_comb = ([], 0)      # (best combination, its value)
    for comb in all_comb:
        weight = 0
        value = 0
        for elem in comb:
            weight += elem[0]
            value += elem[1]
        if weight <= max_weight and value > best_comb[1]:
            best_comb = (comb, value)
    return best_comb[0]

def itemRatio(item):
    return item[1]/item[0]

def heuristicAlgorithm(item_list, max_weight):
    sorted_list = item_list.copy()
    sorted_list.sort(reverse = True, key = itemRatio)
    weight = 0
    final_combination = []
    for elem in sorted_list:
        weight += elem[0]
        if weight > max_weight:
            return final_combination
        else:
            final_combination.append(elem)
    return final_combination

itemList = [(8,16), (3,8), (5,9), (2,6)]
print(bruteForceAlgorithm(itemList, 9))
print(heuristicAlgorithm(itemList, 9))
