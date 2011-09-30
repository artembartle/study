#!/usr/local/bin/python

from math import *

class FWT:
    def __init__(self, values):
        self.values = values
        self.n = 8
        self.result = []
        for i in range(self.n):
            self.result.append(0)
            
    def print_values(self):
        for x in self.result:
            print x    
    
    
    def calculate(self, values):
        n = len(values)
        if n == 1:
            return values
        y = range(n)  
        aEven = []
        aOdd = []    
        for i in range(n):
            if i % 2:
                aOdd.append(values[i])
            else:
                aEven.append(values[i])
                
        bEven = self.calculate(aEven)
        bOdd = self.calculate(aOdd)
        
        j = 0
        while j < n/2:
            y[j] = bEven[j] + bOdd[j]
            y[j + n/2] = bEven[j] - bOdd[j]
            self.mul += 1
            j += 1
        
        return y
        
    def execute(self):
        self.result = self.calculate(self.values)
        if self.rev == -1:
            for i in range(self.n):
                self.result[i] /= self.n
    

def main():
   
   func_values = []
   for i in range(8):
       func_values.append(cos(i)+sin(i))
       print func_values[i]
       
       
if __name__ == "__main__":
    main()
