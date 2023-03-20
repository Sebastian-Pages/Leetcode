class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)

            if c in ")}]":
                if not stack:
                    return False
                closing = stack.pop()

                # check that closing char pairs with last opening char
                if (closing == "(") and (c in "}]"):
                    return False
                if (closing == "{") and (c in ")]"):
                    return False
                if (closing == "[") and (c in "})"):
                    return False

        # Check all pairs are closed   
        if not stack:
            return True
        else:
            return False