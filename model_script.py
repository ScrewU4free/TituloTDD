import tensorflow as tf
import numpy as np

def generate_data():
x = np.random.uniform(-10, 10, size=(1000,1))
y= 3.14 * x + 2.71

x_train, y_train = generate_data()
 
model = tf.keras.Sequential([
tf.keras.layers.dense(1, input_shape=(1,), activation='linear'

model.compile(optimizer='adam', loss='mse')

model.fit(x_train, y_train, epochs=10, verbose=1)

model.save("model")

