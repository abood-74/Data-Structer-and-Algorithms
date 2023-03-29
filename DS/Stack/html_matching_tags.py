"""write a program checking for html tags validty"""

from stack_array_based import Stack
def isValid( code) :
    
    j=code.find("<")    
    stack=Stack()
    while j != -1:                                                      # j will equal -1 if no more tags                                         
        
        k = code.find(">" , j+1)
        if k==-1:
            return False
        
        cur_tag=code[j+1:k]                                             # we want the tag name only so slice untill k (not included)
        if cur_tag[0] != '/':
            stack.push(cur_tag)                                         # store the opening tag to compare it with next closing tag
        
        else:
            if not stack.is_empty() and cur_tag[1:] == stack.top():     # excluding the "/" to compare only the names of tsgs
                stack.pop()
            else:
                return False
        j=code.find("<" , k+1)
    return len(stack) == 0


if __name__ == "__main__":
    stack=Stack()
    code="<html><head><title>hello</title></head><body><h1>hello</h1></body></html>"
    print(isValid(code))
    code="<html><head></title>hello</title></head><body><h1>hello</h1></body></html>"
    print(isValid(code))
