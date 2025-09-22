"""
MSE = 1/n * ∑(Ŷ-Y)^2
"""
import numpy as np
def MSE(prediction:np.ndarray,label:np.ndarray):
    return np.mean((label-prediction)**2)
    
    # for i in range(n):
    #     total += (label[i]-prediction[i])**2
    # if n != 0:
    #     return total/n
    # else: return 0

    # total = [(label[i]-prediction[i])**2 for i in range(n)]
    # return np.sum(total)/n

p = np.array([0,1,2,3,4,5])
l = np.array([1,2,3,4,5,6])
mse = MSE(p,l)
print("MSE: ",mse)