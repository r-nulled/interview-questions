# Return number of consecutive sequences of positive integers summing up to input integer n.
# Example: con_sums(15) = |{[1,5],[4,6],[7,8]}| = 3 

def consecutive_sums(n):
    num_sums = 0
    for i in range(1, n):
        total = i
        for j in range(i + 1, n - i + 1):
            if total + j > n:
                continue
            if total + j = n:
                num_sums += 1
            total += j
    return num_sums

def consecutive_sums_list_comp(n):
    return len([x for x in range(1, n) if len([y for y in range(x, n - x + 1) if sum(range(x, y)) == n]) > 0])