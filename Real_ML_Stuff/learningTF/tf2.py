import tensorflow as tf
from torch import tensor

a = tf.constant([[1,2],[3,4]], dtype=tf.float32)
b = tf.constant([[4,3],[2,1]], dtype=tf.float32)


print(f" result_sum = {tf.add(a,b)} ")
print(f" result_diff = {tf.subtract(a,b)} ")
print(f" result_prod = {tf.multiply(a,b)} ")
print(f" result_div = {tf.divide(a,b)} ")
# Beyond Arithmetic
print(f" result_square = {tf.square(a)} ")
print(f" result_sqrt = {tf.sqrt(a)} ")
print(f" result_exp = {tf.exp(a)} ")
print(f" result_matmul = {tf.matmul(a,b)} ")
print(f" result_log = {tf.math.log(a)} ")
print(f" result_inverse = {tf.linalg.inv(a)} ")
#reduction operations
print(f" result_max = {tf.reduce_max(a)} ")
print(f" result_min = {tf.reduce_min(a)} ")
print(f" result_mean = {tf.reduce_mean(a)} ")

#broadcasting and slicing
print(f" Slicing = {a[0,0]}" ) # type: ignore
result_c = a+b # type: ignore
print(f" Broadcasting = {result_c}")
