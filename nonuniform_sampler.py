import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline

'''
Create sampler class, for a provided normalized distribution "func", within bounds [a,b]. 
'''
class sampler:
    def __init__(self,func,a,b):
        self.a = a
        self.b = b
        self.func = func
        self.y_arr = np.linspace(a,b,int((b-a)/1e-2)) #Make equally spaced array of y values with gap 1e-3
        int_y_arr = []
        for i in range(len(self.y_arr)):
            int_y_arr.append(quad(self.func,a,self.y_arr[i])[0]) #evaluate cumulative distribution integral for the y values
        self.int_y_arr = np.array(int_y_arr)
        self.x_arr = self.int_y_arr*(self.b-self.a) + self.a #evaluate corresponding x values
        self.interp = CubicSpline(self.x_arr,self.y_arr) #interpolate to get y(x)
    
    def sampling(self,x): #returns interpolated value of y sample for given x sample
        if x > self.b or x < self.a:
            raise ValueError(f'{x} is out of distribution bounds [{self.a},{self.b}]') 
        return self.interp(x)

    def samples(self,N,lin_arr=False): #returns set of N y samples, if lin_arr=True then samples are scaled from a linearly spaced set of samples
        if lin_arr == True:
            x_vals = np.linspace(self.a,self.b,N)
        else:
            x_vals = np.random.uniform(self.a,self.b,N)
        samp = []
        for i in range(len(x_vals)):
            samp.append(self.sampling(x_vals[i]))
        return np.array(samp)

'''
Define function to return number of bins according to Freedman Diagonis formula. arr is the array of samples.
'''
#This can be used while making histogram of samples.
def num_bin(arr):
    V = np.array(arr).flatten()
    IQR = np.quantile(V,0.75) - np.quantile(V,0.25)
    Bin_wid = 2*(IQR/(len(V)**(1/3)))
    return int((np.quantile(V,1)-np.quantile(V,0))/Bin_wid)