class Solution:
    def is_valid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if not stack and c in dic.values():
                return False
            elif c in dic:
                stack.append(c)
            elif c != dic.get(stack.pop()):
                return False
        return True and not stack
