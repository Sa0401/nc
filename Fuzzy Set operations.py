import numpy as np
a = np.array(list(map(float, input("Enter fuzzy set A (space-separated): ").split())))
b = np.array(list(map(float, input("Enter fuzzy set B (space-separated): ").split())))
asum = a + b - a * b             
adiff = a + (1 - b)              
aprod = a * b                    
bsum = np.minimum(1, a + b)      
bdiff = np.maximum(0, a - b)    
bprod = np.maximum(0, a + b - 1) 
print("The algebraic sum:", asum)
print("The algebraic difference:", adiff)
print("The algebraic product:", aprod)
print("The bounded sum:", bsum)
print("The bounded difference:", bdiff)
print("The bounded product:", bprod)

