#!/usr/local/bin/python

from pylab import *

class FWT:
    def __init__(self, values, rev = 1):
        self.values = values
        self.n = 8
        self.result = []
        self.rev = rev
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
        first_half = []
        sec_half = []    
        for i in range(n/2):
            first_half.append(values[i])
            sec_half.append(values[i + n/2])

                
        b_first = self.calculate(first_half)
        b_sec = self.calculate(sec_half)
        
        j = 0
        while j < n/2:
            y[j] = b_first[j] + b_sec[j]
            y[j + n/2] = b_first[j] - b_sec[j]
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
        
    walsh = FWT(func_values)
    walsh.execute()
    walsh.print_values()
       
    walsh_rev = FWT(walsh.result, -1)
    walsh_rev.execute()
    walsh_rev.print_values()
    
    x = arange(0.0, 7.0, 0.1)
    subplot(311)
    plot(x, cos(x)+sin(x), range(8), walsh.values, 'go')
    grid(True)
    
    subplot(312)
    plot(range(0.0, 2*pi*7, 2*pi), walsh.result, 'r--', range(0.0, 2*pi*7, 2*pi), walsh.result, 'go')
    grid(True)
    
    subplot(313)
    plot(range(8), walsh_rev.result, 'r--', range(8), walsh_rev.result, 'go')
    grid(True)
    
    show()
    
if __name__ == "__main__":
    main()
