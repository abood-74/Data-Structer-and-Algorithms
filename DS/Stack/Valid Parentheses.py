"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1-Open brackets must be closed by the same type of brackets.
2-Open brackets must be closed in the correct order.
3-Every close bracket has a corresponding open bracket of the same type.
"""

from stack_array_based import Stack

def is_valid(s: str) -> bool:
        
    right = '])}'
    left = '[({'
    stack = Stack()
    
    for i in s:
        
        if i in left:
            stack.push(i)
        else:
            if len(stack) == 0:                                            
                    return False                                                        # because stack is empty and the right bracket wont math any left bracket
            elif right.find(i) != left.find(stack.pop()):                               # if the brackets match each other it should has same index at right and left strings 
                    return False
                
    return stack.is_empty()       




if __name__ == "__main__":
    print(is_valid("()"))
    print(is_valid("())()"))
    print(is_valid("[(()]"))
    
    