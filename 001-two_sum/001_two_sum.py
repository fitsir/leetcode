class Solution(object):

    def twoSum(self, nums, target):
        # 击败12.8%的python提交
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        else:
            return None

    def twoSum1(self, nums, target):
        # 击败36.62%的python提交
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            vs = set(map.keys())
            if complement in vs:
                return [map[complement], i]
            map[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    r = s.twoSum1(nums, target)
    print(r)
    pass
