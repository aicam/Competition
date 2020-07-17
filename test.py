from TrainUtils.preprocess_data import *
import pandas as pd
import tensorflow as tf
from TrainUtils.model import *
my_callbacks = [tf.keras.callbacks.ModelCheckpoint(filepath='{epoch:02d}-{val_loss:.2f}.h5',monitor='val_loss',
                                                save_best_only=True),
                tf.keras.callbacks.TensorBoard(log_dir='./logs')]
model, feature_model = build_network()

df = pd.read_csv('processed_data/' + str(0*200) + '.csv')
learning_cols = [it for it in df.columns if it.__contains__('lead')]
arr = convert_df(df[learning_cols].to_numpy())
X = padding(arr)
labels_df = pd.read_csv('./supporting_materials/snomed_ct_codes.csv')
labels = dict((e, 0) for e in labels_df['SNOMED CT Code'])
Y = get_labels_array(labels, df['Dx'].to_numpy())
print(X.shape)
history = model.fit(
    np.array(X), np.array(Y),
    epochs=100,
    callbacks=my_callbacks
)