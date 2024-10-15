# A teacher is writing a test with n true/false questions, with 'T' denoting
# true and 'F' denoting false. He wants to confuse the students by maximizing the
# number of consecutive questions with the same answer (multiple trues or multiple
# falses in a row).
#
#  You are given a string answerKey, where answerKey[i] is the original answer
# to the iᵗʰ question. In addition, you are given an integer k, the maximum number
# of times you may perform the following operation:
#
#
#  Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i]
# to 'T' or 'F').
#
#
#  Return the maximum number of consecutive 'T's or 'F's in the answer key
# after performing the operation at most k times.
#
#
#  Example 1:
#
#
# Input: answerKey = "TTFF", k = 2
# Output: 4
# Explanation: We can replace both the 'F's with 'T's to make answerKey =
# "TTTT".
# There are four consecutive 'T's.
#
#
#  Example 2:
#
#
# Input: answerKey = "TFFT", k = 1
# Output: 3
# Explanation: We can replace the first 'T' with an 'F' to make answerKey =
# "FFFT".
# Alternatively, we can replace the second 'T' with an 'F' to make answerKey =
# "TFFF".
# In both cases, there are three consecutive 'F's.
#
#
#  Example 3:
#
#
# Input: answerKey = "TTFTTFTT", k = 1
# Output: 5
# Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
# Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT".
# In both cases, there are five consecutive 'T's.
#
#
#
#  Constraints:
#
#
#  n == answerKey.length
#  1 <= n <= 5 * 10⁴
#  answerKey[i] is either 'T' or 'F'
#  1 <= k <= n
#
#
#  Related Topics String Binary Search Sliding Window Prefix Sum 👍 2894 👎 46


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # TTTTFFTT
        n = len(answerKey)
        max_len = 1
        for letter in 'TF':
            left = 0
            count = 0
            ku = 0
            for i, c in zip(range(n), answerKey):
                if c == letter:
                    count += 1
                elif ku < k:
                    ku += 1
                    count += 1
                else:
                    # clear left part
                    for l in range(left, i):
                        if letter != answerKey[l]:
                            left = l + 1
                            break
                    count = i - left + 1
                max_len = max(count, max_len)
        return max_len


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    for answerKey, k, ans in [
        ['TTFTTFTT', 1, 5],
        ['TFFF', 1, 4],
        ['FFFTTFTTFT', 3, 8],
        ['TTFF', 2, 4],
        ['TFFT', 1, 3],
        ['TTFFTTFFTT', 2, 6],
        ['TTFFTTFFTT', 4, 10],
        ['TTFFTTFTTFFT', 5, 12],
        ['TTFFTTFFTT', 2, 6],
        ['TTFFFTTFFTTFFTTT', 7, 16],
    ]:
        result = s.maxConsecutiveAnswers(answerKey, k)
        if result != ans:
            print('error:', answerKey, k, ans, result)
