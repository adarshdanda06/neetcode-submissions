class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        hash_map  = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for i in s:
            if i != ')' and i != '}' and i != ']':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                var = stack.pop()
                if hash_map[i] != var:
                    return False
        if len(stack) > 0:
            return False
        return True
    
            
            