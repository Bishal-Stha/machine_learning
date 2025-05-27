import tensorflow as tf

tensor = tf.constant("Hello, Tensorflow!")

print(tensor.numpy().decode())   # type: ignore # tensor.numpy() gives bytes, decode to string
