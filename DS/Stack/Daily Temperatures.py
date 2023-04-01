"""Given an array of integers temperatures represents the daily temperatures, 
    return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
    If there is no future day for which this is possible, keep answer[i] == 0 instead
"""
from stack_array_based import Stack
def dailyTemperatures(temperatures) :
    
    s = Stack()
    answer = [0] * len(temperatures)
    for i in range(len(temperatures)):
        while len(s) > 0  and temperatures[s.top()] < temperatures[i]:                # if the temperature became warmer compare it with the top element of stack untill you find bigger value in stack or stack become empty
            answer[s.top()] = i - s.top()                                             # update the value of the day by accesing its index
            s.pop()
        
        s.push(i)                                                                      # store  idices in the stack so the elements can be compared easily 
    return answer

if __name__ == "__main__":

    print(dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(dailyTemperatures([30,40,50,60]))
    print(dailyTemperatures([30,60,90]))



            
            
            
        