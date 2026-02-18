def permute(num: str) -> list[int]:
    digits = list(num)
    # digits = [int(digit) for digit in digits]

    def helper(nums: list) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = helper(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res

    permutations = helper(digits)
    ans = []

    for permutation in permutations:
        ans.append(int(str("".join(permutation))))
    return ans  


# permutated_list = permute('0123456789')
# permutated_list.sort()

# print(permutated_list[999999])