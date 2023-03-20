class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):

            if digits[len(digits) - i - 1] == 9:
                digits[len(digits) - i - 1] = 0
                if i == len(digits) - 1:
                    digits.insert(0, 1)
                    return digits
            else:
                digits[len(digits) - i - 1] += 1
                return digits