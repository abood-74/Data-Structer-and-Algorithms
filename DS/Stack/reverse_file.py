"""Write a program that reveses lines in file."""
import os
from stack_array_based import Stack
def reverse_ﬁle(ﬁlename):
    S = Stack()
    original = open(ﬁlename)
    
    for line in original:                               # we will re-insert newlines when writing
        S.push(line.rstrip( "\n" ))
    original.close( )
    # now we overwrite with contents in LIFO order
    # reopening ﬁle overwrites original
    output = open(ﬁlename, "w" )
    while not S.is_empty( ):
        output.write(S.pop( ) + "\n ")                   # re-insert newline characters

    output.close( )
    
    
    
if __name__ == "__main__":
    # Get the current working directory
    cwd = os.getcwd()

    # Construct the file path
    test = os.path.join(cwd, 'DS/Stack/test.txt')
    # before reversing
    with open(test) as file:
        for line in file:
            print(line)
    reverse_file(test)
    print("//////////////////////\n")
    # after reversing
    with open(test) as file:
            for line in file:
                print(line)