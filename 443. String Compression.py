from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        currentPos = 0
        lastCount = 0
        for pos, symbol in enumerate(chars):
            if pos == 0:
                lastCount = 1
                continue
            if pos > 0 and symbol != chars[pos - 1]:
                chars[currentPos] = chars[pos - 1]
                currentPos += 1
                if lastCount > 1:
                    for digit in str(lastCount):
                        chars[currentPos] = digit
                        currentPos += 1
                lastCount = 1
            else:
                lastCount += 1
        chars[currentPos] = symbol
        currentPos += 1
        if lastCount > 1:
            for digit in str(lastCount):
                chars[currentPos] = digit
                currentPos += 1
        return currentPos