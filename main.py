input_dir = 'dataset/'
import tensorflow as tf
import pandas as pd
from TrainUtils.model import *
callbacks = [tf.keras.callbacks.ModelCheckpoint(filepath='best_model.h5',
                                            monitor='val_loss',
                                            save_best_only=True), ]
# model, feature_model = build_network()
# X_train, Y_train, X_test, Y_test = [], [], [], []
# history = model.fit(
#     X_train, Y_train,
#     epochs=100,
#     callbacks=callbacks,
# )
df = pd.read_hdf('store.h5')
