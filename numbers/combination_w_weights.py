"""
Given 4 separate lists of prices (A_1, A_2, A_3, A_4), each for a different product (eg hats, shoes, shirts, and pants), how many combinations (sets of clothing including 1 item from each product category) can one make
given a (budget) total price limitation of B?

example input:

hats: [1, 2, 3]
shoes: [2, 3, 4]
pants: [1,3, 5]
shirts: [1, 2]

[1,2][3,4][5,6][7,8]

[1,3][1,4][2,3][2,4],[5,7][5,8][6,7][6,8]


Simple solution:
Find and check every possible combination. Time complexity: O(klmn)*O(1)

Better solutions:
- Dynamic programming is a tempting tool to reach for, but the potentially large input size of B makes it very memory expensive.

- We want to avoid testing all klmn combinations.
- We can merge our four lists into two list of (hat, shoes) and (pants, shirts) combinations in O(kl) + O(mn) time.
- We map the prices of the two combined lists onto a hashmap of (price : number of combinations)
- For each price pair between the two lists satisfying the budgetary constraint, add the product to the total.
- Run time is now contingent not upon the length of the lists, but the prices of the items: O(max(price_1*price_2)*max(price_3*price*4))
"""
def inc_counts(counter, prices):
        for price in prices:
            counter[price] = counter.get(price, default = 0) + 1

def num_combinations(one,two,three,four,budget):
    merge_one_two = [a + b for b in one for a in two]
    merge_three_four = [c + d for c in three for d in four]

    map_ot = {}
    map_tf = {}

    def inc_counts(counter, prices):
        for price in prices:
            counter[price] = counter.get(price, 0) + 1
    
    inc_counts(map_ot, merge_one_two)
    inc_counts(map_tf, merge_three_four)

    total = 0
    for price_a in sorted(map_ot.keys()):
        for price_b in reversed(range(1, budget - price_a + 1)):
            total += map_ot[price_a] * map_tf.get(price_b, 0)

    return (total, map_ot, map_tf)

hats =  [1, 2, 3]
shirts = [1, 2]

shoes = [2, 3, 4]
pants = [1,3, 5]

