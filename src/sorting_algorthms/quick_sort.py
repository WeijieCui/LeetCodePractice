import random


def quick_sort(nums: []):
    def qs(s, e):
        if e - s < 2:
            return
        elif e - s == 2:
            if nums[s] > nums[e - 1]:
                nums[s], nums[e - 1] = nums[e - 1], nums[s]
            return
        m = int((s + e) / 2)
        small = []
        big = []
        for n in nums[s: e]:
            if n < nums[m]:
                small.append(n)
            elif n > nums[m]:
                big.append(n)
        # print(nums[s:e], ls + [nums[m]] * (e - s - len(ls) - len(ll)) + ll)
        nums[s:e] = small + [nums[m]] * (e - s - len(small) - len(big)) + big
        if len(small) > 1:
            qs(s, s + len(small))
        if len(big) > 1:
            qs(e - len(big), e)

    qs(0, len(nums))
    return nums


if __name__ == '__main__':
    # print(quick_sort([3, 2, 1, 5, 4, 6]))
    for i in range(1000):
        ls = [random.randint(-1 << 31, (1 << 31) - 1) for _ in range(10000)]
        ans = quick_sort(ls)
        if ans != sorted(ls):
            print('error occur: ', ans)
        if i % 100 == 0:
            print(ans[:10])
    print(quick_sort([3, 2, 1, 5, 4, 6, 8, 9, 3, 2, 12, 15, 32, -1, -10, 0, (1 << 31) - 1, -(1 << 31)]))
    print(quick_sort([1]))
    print(quick_sort([]))
    print(quick_sort([3, 2, 1]))
