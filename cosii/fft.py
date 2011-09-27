#!/usr/local/bin/python

from pylab import *
from numpy import fft

class Transform:
    def __init__(self, values, rev = 1):
        self.rev = rev
        self.values = values
        self.n = 8
        self.result = []
        self.mul = 0
        self.amp = []
        self.phase = []
        for i in range(self.n):
            self.result.append(complex(0, 0))
        
    def fill_spectres(self):
        for i in range(self.n):
            x = self.result[i]
            self.amp.append(sqrt(pow(x.real, 2) + pow(x.imag, 2)))
            self.phase.append(math.atan(x.imag/x.real))
            
    def print_values(self):
        print self.__class__
        print 'mul operations:{0}'.format(self.mul)
        for x in self.result:
            print x

class DFT(Transform):
    def calculate(self, k):
        w = exp(-1j*2*pi/self.n)
        res = complex(0, 0)
        for i in range(self.n):
            res += self.values[i] * (w ** (self.rev * k * i))
            self.mul += 1
        if self.rev == -1:
            return res / self.n
        return res
    
    
    def execute(self):
        for i in range(self.n):
            self.result[i] = self.calculate(i)
                
class FFT(Transform):
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
        
        wn = exp(1j*2*pi*self.rev/n)
        w = 1
        j = 0
        while j < n/2:
            y[j] = bEven[j] + w * bOdd[j]
            y[j + n/2] = bEven[j] - w * bOdd[j]
            w = w * wn
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
       func_values.append(complex(cos(i)+sin(i), 0))
       print func_values[i]
       
       
   fast = FFT(func_values)
   fast.execute()
   fast.print_values()
   fast.fill_spectres()
   
   discrete = DFT(func_values)
   discrete.execute()
   discrete.print_values()
   
   fast_revers = FFT(fast.result, -1)
   fast_revers.execute()
   fast_revers.print_values()
   
   x = arange(0.0, 8.0, 0.1)
   subplot(511)
   plot(x, cos(x)+sin(x), range(8), fast.values, 'go')
   grid(True)
   
   subplot(512)
   plot(range(0.0, 2*pi*7, 2*pi), fast.result, 'r--', range(0.0, 2*pi*7, 2*pi), fast.result, 'go')
   grid(True)
   
   subplot(513)
   plot(range(8), fast_revers.result, 'r--', range(8), fast_revers.result, 'go')
   grid(True)   
   
   subplot(514)
   plot(range(0.0, 2*pi*7, 2*pi), fast.amp, 'go')
   grid(True)
   subplot(515)
   plot(range(0.0, 2*pi*7, 2*pi), fast.phase, 'r.')
   grid(True)
   show()
"""        
   
   
   subplot(212)
   title('Image:')
   plot(range(0.0, 2*pi*7, 2*pi), fast.result, 'r--', range(0.0, 2*pi*7, 2*pi), fast.result, 'go')
   grid(True)

   show()
"""
if __name__ == "__main__":
    main()
