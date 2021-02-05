import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist

(x_train,y_train),(x_test,y_test)= tf.keras.datasets.mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))

EPOCHS = 10
checkpoint_filepath = '/tmp/checkpoint'

model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_filepath,
    save_weights_only=True,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True)
early_stopping_callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=['accuracy'])
model.fit(x_train,y_train,epochs=4,callbacks=[model_checkpoint_callback,early_stopping_callback])
val_loss, val_acc = model.evaluate(x_test,y_test)
model.load_weights(checkpoint_filepath)

m_name = "mnist_numbers.model"
model.save(m_name)
