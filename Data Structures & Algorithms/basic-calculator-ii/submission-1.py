class Solution:
    def calculate(self, s: str) -> int:
        p_s = s.replace(" ", "")
        p = 0
        last_var = None
        last_op = None
        processed_res = ""
        # 20+
        # 20+5/3*2-1
        # 14-3/2
        # 
        while p < len(p_s):
            temp = ""
            while p < len(p_s) and p_s[p].isnumeric():
                temp += p_s[p]
                p += 1

            curr_int = int(temp)
            if last_op == "*":
                curr_int = last_var * curr_int
            if last_op == "/":
                curr_int = last_var // curr_int

            if p >= len(p_s) or p_s[p] == "+" or p_s[p] == "-":
                processed_res += str(curr_int)

            if p < len(p_s):
                if p_s[p] == "+" or p_s[p] == "-":
                    processed_res += p_s[p]
                else:
                    last_var = curr_int                
                last_op = p_s[p]

            p += 1
        print(processed_res)
        
        ans = 0
        last_op = "+"
        i = 0
        while i < len(processed_res):
            temp = ""
            while i < len(processed_res) and processed_res[i].isnumeric():
                temp += processed_res[i]
                i += 1

            curr = int(temp)

            if last_op == "+":
                ans += curr
            else:
                ans -= curr

            if i < len(processed_res):
                last_op = processed_res[i]
            i += 1

        return ans

