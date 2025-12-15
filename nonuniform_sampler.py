import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline

class sampler:
    def __init__(self,func,a,b):
        self.a = a
        self.b = b
        self.func = func
        self.y_arr = np.linspace(a,b,int((b-a)/1e-2)) #Make equally spaced array of y values with gap 1e-3
        int_y_arr = []
        for i in range(len(self.y_arr)):
            int_y_arr.append(quad(self.func,a,self.y_arr[i])[0])
        self.int_y_arr = np.array(int_y_arr)
        self.x_arr = self.int_y_arr*(self.b-self.a) + self.a
        self.interp = CubicSpline(self.x_arr,self.y_arr)
    
    def sampling(self,x):
        if x > self.b or x < self.a:
            raise ValueError(f'{x} is out of distribution bounds [{self.a},{self.b}]') 
        return self.interp(x)

    def samples(self,_x_vals):
        x_vals = np.array(_x_vals)
        samp = []
        for i in range(len(x_vals)):
            samp.append(self.sampling(x_vals[i]))
        return np.array(samp)

'''
Define function to return number of bins according to Freedman Diagonis formula. arr is the array of samples.
'''

def num_bin(arr):
    V = np.array(arr).flatten()
    IQR = np.quantile(V,0.75) - np.quantile(V,0.25)
    Bin_wid = 2*(IQR/(len(V)**(1/3)))
    return int((np.quantile(V,1)-np.quantile(V,0))/Bin_wid)