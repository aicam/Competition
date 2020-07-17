from TrainUtils.preprocess_data import *

input_dir = 'dataset/'
import tensorflow as tf
import pandas as pd
from TrainUtils.model import *
callbacks = [tf.keras.callbacks.ModelCheckpoint(filepath='best_model.h5',
                                            monitor='val_loss',
                                            save_best_only=True), ]
model, feature_model = build_network()
df = pd.read_csv('processed_data/0.csv')
learning_cols = [it for it in df.columns if it.__contains__('lead')]
arr = convert_df(df[learning_cols].to_numpy())
X = padding(arr)

labels_df = pd.read_csv('./supporting_materials/snomed_ct_codes.csv')
labels = dict((e, 0) for e in labels_df['SNOMED CT Code'])


for i in range(20):
    X_train, Y_train = df[], []
    history = model.fit(
        X_train, Y_train,
        epochs=100,
        callbacks=callbacks,
    )
df = pd.read_hdf('store.h5')
