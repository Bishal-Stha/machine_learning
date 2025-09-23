import random

# # Basic numbers
print(random.random())       # [0.0, 1.0)
print(random.randint(1, 10)) # [1, 10]
print(random.randrange(0, 10, 2))  # even numbers 0–8

# # From sequences
items = ['apple', 'banana', 'cherry']
print(random.choice(items))       # pick 1 random
print(random.sample(items, 2))    # pick 2 unique
random.shuffle(items)             # shuffle in-place
print(items)

# # Continuous distributions
print(random.uniform(1, 5))       # float [1, 5]
print(random.gauss(0, 1))         # Gaussian(mean=0, std=1)
print(random.expovariate(1/5))    # Exponential distribution

# # Seed (for reproducibility)
random.seed(42)
print(random.randint(1, 100))     # same result each run
