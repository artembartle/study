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

def convolution(x_values, y_values):
    fft_x = FFT(x_values)
    fft_x.execute()
    fft_y = FFT(y_values)
    fft_y.execute()
    z_values = []
    for i in range(len(x_values)):
        z_values.append(fft_x.result[i] * fft_y.result[i])
        
    result = FFT(z_values, -1)
    result.execute()
    result.print_values()
    return result

def main():
    x,y = [], []
    for i in range(8):
        x.append(complex(cos(i), 0))
        y.append(complex(sin(i), 0))
    
    z = convolution(x,y)


    x = arange(0.0, 8.0, 0.1)
    subplot(311)
    plot(x, cos(x))
    grid(True)
    title('y=cos(x)')
   
    subplot(312)
    title('z=sin(x)')
    plot(x, sin(x))
    grid(True)
    
    subplot(313)
    title('Convolution:')
    plot(range(0.0, 2*pi*7, 2*pi), z.result, 'r--')

    show()

if __name__ == "__main__":
    main()
