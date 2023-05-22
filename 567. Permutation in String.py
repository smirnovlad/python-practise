class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        diff_count = 0
        arr = [0 for _ in range(26)]

        for symbol in s1:
            i = ord(symbol) - ord('a')
            arr[i] += 1
            if arr[i] == 1:
                diff_count += 1

        for i in range(len(s1)):
            symbol = s2[i]
            j = ord(symbol) - ord('a')
            arr[j] -= 1
            if arr[j] == 0:
                diff_count -= 1
            elif arr[j] == -1:
                diff_count += 1

        if diff_count == 0:
            return True

        for i in range(len(s1), len(s2)):
            symbol_to_drop = s2[i - len(s1)]
            j = ord(symbol_to_drop) - ord('a')
            arr[j] += 1
            if arr[j] == 0:
                diff_count -= 1
            elif arr[j] == 1:
                diff_count += 1

            symbol_to_add = s2[i]
            j = ord(symbol_to_add) - ord('a')
            arr[j] -= 1
            if arr[j] == 0:
                diff_count -= 1
            elif arr[j] == -1:
                diff_count += 1

            if diff_count == 0:
                return True

        return False

solver = Solution()
print(solver.checkInclusion(s1 = "ab", s2 = "eidboaoo"))