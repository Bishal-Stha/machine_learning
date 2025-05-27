import tensorflow as tf

a = tf.constant(100)
b = tf.constant(20)

add_op = tf.add(a,b)
sub_op = tf.subtract(a,b)
prod_op = tf.multiply(a,b)
div_op = tf.divide(a,b)

print("Sum is ", add_op.numpy())
print("Sub is ", sub_op.numpy())
print("Prod is ", prod_op.numpy())
print("Div is ", div_op.numpy())
