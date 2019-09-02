def sum_pairs(ints, s):
    memo = {}
    for i in ints:
        if i in memo:
            return [memo[i], i]
        memo[s-i] = i
    return None

