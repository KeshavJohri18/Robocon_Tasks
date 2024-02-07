class Solution:
    def isValid(self, s: str) -> bool:

        char_list = [i for i in s]

        left = ["(", "[", "{"]
        right = [")", "]", "}"]

        j = 0
        
        STACK = []

        while(j < len(char_list)):
            
            if (char_list[j] in left):
                STACK.append(char_list[j])
            
            else:
                if not STACK:
                    return False

                if(char_list[j] == right[0]):
                    if(STACK[-1] != left[0]):
                        return False

                if(char_list[j] == right[1]):
                    if(STACK[-1] != left[1]):
                        return False

                if(char_list[j] == right[2]):
                    if(STACK[-1] != left[2]):
                        return False

                STACK.pop()
                               
            j += 1

        if not STACK:
            return True
        
        return False
