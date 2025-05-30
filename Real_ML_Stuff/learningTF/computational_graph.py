import tensorflow as tf

@tf.function
def matmul_graph():
    a = tf.constant([[1, 2], [3, 4]])
    b = tf.constant([[5, 6], [7, 8]])
    return tf.matmul(a, b)

# Get concrete function and print graph operations
concrete_func = matmul_graph.get_concrete_function()
for op in concrete_func.graph.get_operations():  # type: ignore
    print(op.name)
