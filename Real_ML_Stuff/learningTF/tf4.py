import tensorflow as tf

#create a tensorflow graph
graph = tf.Graph()


with graph.as_default():
    a = tf.constant(10)
    b = tf.constant(20)
    c = tf.add(a,b)
