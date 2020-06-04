# --------------
import pandas as pd
import numpy as np
import math


#Code starts here
class complex_numbers:
    def __init__(self, r, i):
        self.real=r
        self.imag=i
    def __repr__(self):
        if self.real==0.0 and self.imag==0.0:
            return "0.00"
        if self.real==0:
            return '%.2fi' % self.imag
        if self.imag==0:
            return '%.2f' % self.real
        return '%.2f %s %.2fi' % (self.real,'+' if self.imag>=0 else '-',abs(self.imag))
    def __add__(self, other):
        a=self.real+other.real
        b=self.imag+other.imag
        return complex_numbers(a,b)
    def __sub__(self, other):
        a=self.real-other.real
        b=self.imag-other.imag
        return complex_numbers(a,b)
    def __mul__(self, other):
        a=self.real*other.real-self.imag*other.imag
        b=self.real*other.imag+self.imag*other.real
        return complex_numbers(a,b)
    def __truediv__(self, other):
        denom=int(other.real**2+other.imag**2)
        a=(self.real*other.real+self.imag*other.imag)/denom
        b=(self.imag*other.real-self.real*other.imag)/denom
        return complex_numbers(a,b)
    def absolute(self):
        ab=math.sqrt(self.real**2+self.imag**2)
        return ab
    def argument(self):
        arg=math.atan2(self.imag,self.real)
        return np.degrees(arg)
    def conjugate(self):
        return complex_numbers(self.real,-1*self.imag)

comp_1=complex_numbers(3,5)
comp_2=complex_numbers(4,4)
comp_sum=comp_1.__add__(comp_2)
comp_diff=comp_1.__sub__(comp_2)
comp_prod=comp_1.__mul__(comp_2)
comp_quot=comp_1.__truediv__(comp_2)
comp_abs=comp_1.absolute()
comp_conj=comp_1.conjugate()
comp_arg=comp_1.argument()
print(comp_arg)
    



