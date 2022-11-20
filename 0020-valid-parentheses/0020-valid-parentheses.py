class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            "(": ")", 
            "{": "}", 
            "[": "]"
        }
        
        for char in s:
            if char in parentheses:
                stack.append(char)
            elif len(stack) > 0 and char == parentheses[stack[len(stack) - 1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
