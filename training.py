import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
import time
(x_train,y_train),(x_test,y_test)= tf.keras.datasets.mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))

EPOCHS = 20

early_stopping_callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=['accuracy'])
model.fit(x_train,y_train,epochs=EPOCHS ,callbacks=[early_stopping_callback])
val_loss, val_acc = model.evaluate(x_test,y_test)
m_name = "mnist_numbers.model"
model.save(m_name)
