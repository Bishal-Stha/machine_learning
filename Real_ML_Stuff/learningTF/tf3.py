import tensorflow as tf

# Create a constant tensor
constant_tensor = tf.constant([1,2,3,4,5])
print(constant_tensor)

#Create a variable tensor with initial values
initial_value = tf.random.normal(shape= (3,3))
variable_tensor = tf.Variable(initial_value)
print(variable_tensor)

# Updatea variable tensor
new_values = tf.random.normal(shape =(3,3))
variable_tensor.assign(new_values)
print(variable_tensor)