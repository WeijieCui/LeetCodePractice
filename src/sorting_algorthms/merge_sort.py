def merge_sort(nums: []):
    def merge(nums1, nums2):
        i, j = 0, 0
        ls = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ls.append(nums1[i])
                i += 1
            else:
                ls.append(nums2[j])
                j += 1
        if i < len(nums1):
            ls.extend(nums1[i:])
        elif j < len(nums2):
            ls.extend(nums2[j:])
        return ls

    if not nums:
        return []

    old_list = [[i] for i in nums]
    while len(old_list) > 1:
        combines = []
        # merge
        for i in range(int(len(old_list) / 2)):
            combines.append(merge(old_list[i * 2], old_list[i * 2 + 1]))
        if len(old_list) % 2 == 1:
            combines.append(old_list[-1])
        old_list = combines
    return old_list[0]


if __name__ == '__main__':
    print(merge_sort([3, 5, 6, 2, 1, 12]))
    print(merge_sort([]))
    print(merge_sort(None))
    print(merge_sort([1]))
