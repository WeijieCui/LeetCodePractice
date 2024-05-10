# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers 
# sum to target. You may return the combinations in any order. 
# 
#  The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen 
# numbers is different. 
# 
#  The test cases are generated such that the number of unique combinations 
# that sum up to target is less than 150 combinations for the given input. 
# 
#  
#  Example 1: 
# 
#  
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple 
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#  
# 
#  Example 3: 
# 
#  
# Input: candidates = [2], target = 1
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 30 
#  2 <= candidates[i] <= 40 
#  All elements of candidates are distinct. 
#  1 <= target <= 40 
#  
# 
#  Related Topics Array Backtracking 👍 18512 👎 406


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates, reverse=True)
        cache = {}

        def combine(idx: int, t: int) -> [[int]]:
            key = (idx, t)
            if key in cache:
                return [[*s] for s in cache[key]]
            val = candidates[idx]
            times = int(t / val)
            if idx == len(candidates) - 1:
                combinations = [[val] * times] if t % val == 0 and times > 0 else []
                cache.setdefault(key, [[*s] for s in combinations])
                return combinations
            else:
                combinations = []
                for i in range(times + 1):
                    rest = t - val * i
                    sub_combinations = combine(idx + 1, rest) if rest >= candidates[-1] else []
                    for c in sub_combinations:
                        c.extend((val for i in range(i)) if i > 0 else [])
                    if rest == 0 and i != 0:
                        sub_combinations.append([val] * i)
                    combinations.extend(sub_combinations)
                cache.setdefault(key, [[*s] for s in combinations])
                return combinations

        return combine(0, target)
# leetcode submit region end(Prohibit modification and deletion)
