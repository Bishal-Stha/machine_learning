import math

# Constants
print(math.pi)      # 3.141592653589793
print(math.e)       # 2.718281828459045

# Rounding & absolute
print(math.ceil(3.2))   # 4 (round up)
print(math.floor(3.8))  # 3 (round down)
print(math.trunc(3.8))  # 3 (cut decimal, no round)

# Power & roots
print(math.sqrt(16))      # 4.0
print(math.pow(2, 3))     # 8.0 (float)
print(2 ** 3)             # 8 (faster, int or float)

# Logarithms
print(math.log(8, 2))     # 3.0 (log base 2)
print(math.log10(100))    # 2.0
# print(f"log5 25: {math.log(125,5)}")
print(math.log(125,5))

# Trigonometry
print(math.sin(math.pi/2)) # 1.0
print(math.cos(0))         # 1.0
print(math.degrees(math.pi/2)) # 180.0
print(math.radians(90))     # 1.5707

# Factorial & combinations
print(math.factorial(5))     # 120
print(math.comb(5, 2))       # 10
print(math.perm(5, 2))       # 20

a,b = 0.1, 0.2
c = a+b
print(a+b)
print(a+b ==c)
print(math.isclose(a+b,c,rel_tol=1e-9))
