class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ele in s:
            if(ele=='(' or ele=='[' or ele=='{'):
                stack.append(ele)

            elif ele==')' and (not stack or stack[-1]!='('):
                return False
            elif ele==']' and (not stack or stack[-1]!='['):
                return False
            elif ele=='}' and (not stack or stack[-1]!='{'):
                return False

            else:
                stack.pop()


        return len(stack)==0

            


         
        