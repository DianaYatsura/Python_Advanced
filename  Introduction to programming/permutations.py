"""
Given two permutations p and q of length n. Find a permutation r, such that for every 1 <= i <= n, q[i] = p[r[i]].
Permutation of length n is an array consisting of distinct numbers from 1 to n in some order.
Example
Input:

Output:
r = [3, 2, 1]
[input] array.integer p
[input] array.integer q
[output] array.integer
permutation r
"""
def find_permutation(p, q):
    r = []
    p_dict = {v: k +1 for k,v in enumerate(p)}
    for x in q:
        r.append(p_dict[x])
    return r


p = [3, 4, 1, 2, 5]
q = [4, 5, 2, 3, 1]

print(find_permutation(p,q)) #[2, 5, 4, 1, 3]
