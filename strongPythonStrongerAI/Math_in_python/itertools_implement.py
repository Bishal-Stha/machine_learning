from itertools import count, cycle, repeat, permutations, combinations, chain, product

for i in count(1,3):
    # if i < 20: print(i) 
    # else: break
    if i >20: break
    print(i)

animals = cycle(["1. tiger","2. leopard","3. Deer","4. Elephant"])
for _ in range(10):
    print(next(animals))

for message in repeat("Hello there",3):
    print(message)

print(list(chain([1,2], [3,4], [5])))

print(list(permutations([1,2,3],2)))
print(list(combinations([1,2,3],2)))

# Cartesian Product
setA = {"A","B","C"}
setB = {1,2,3}
print(list(product(setA, setB)))

#######################
from itertools import accumulate

nums = [1,2,3,4] 
print(list(accumulate(nums)))              # [1, 3, 6, 10] # Cumulative Sum


