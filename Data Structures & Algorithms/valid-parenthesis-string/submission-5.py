class Solution:
    def checkValidString(self, s: str) -> bool:
        #first lets check if even possible
        hash_map = {
            ')': 0,
            '(': 0,
            '*': 0
        }
        for i in s:
            hash_map[i] += 1
        
        if min(hash_map['('], hash_map[')']) + hash_map['*'] < max(hash_map['('], hash_map[')']):
            return False
        
        #( stack: 0, 1, 2
        #* stack: 3
        #) stack: 4
        op_stack = []
        st_stack = []
        cl_stack = []

        #at end: open and close stack should both be empty
        for i in range(len(s)):
            if s[i] == '(':
                op_stack.append(i)
            elif s[i] == '*':
                st_stack.append(i)
            else:
                if len(op_stack) > 0:
                    op_stack.pop()
                elif len(st_stack) > 0:
                    st_stack.pop()
                else:
                    return False

        print(op_stack)
        print(st_stack)
        while len(op_stack) > 0:
            if len(st_stack) > 0:
                if op_stack.pop() > st_stack.pop():
                    return False
            else:
                return False


        return True