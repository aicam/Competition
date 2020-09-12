from .config import *
import tensorflow as tf
import keras.backend as K
import tensorflow_addons as tfa
from keras.layers import Dense, Convolution1D, GlobalAveragePooling2D, MaxPool1D, Flatten, Dropout
from keras.layers import Input
from keras.layers.normalization import BatchNormalization

from keras.models import Model

def f1_loss(y_true, y_pred):

    tp = K.sum(K.cast(y_true*y_pred, 'float'), axis=0)
    tn = K.sum(K.cast((1-y_true)*(1-y_pred), 'float'), axis=0)
    fp = K.sum(K.cast((1-y_true)*y_pred, 'float'), axis=0)
    fn = K.sum(K.cast(y_true*(1-y_pred), 'float'), axis=0)

    p = tp / (tp + fp + K.epsilon())
    r = tp / (tp + fn + K.epsilon())

    f1 = 2*p*r / (p+r+K.epsilon())
    f1 = tf.where(tf.math.is_nan(f1), tf.zeros_like(f1), f1)
    return 1 - K.mean(f1)




def build_network():
    im_shape= CNNInputShape
    inputs_cnn=Input(shape=(im_shape), name='inputs_cnn')
    conv1_1=Convolution1D(64, (6), activation='relu', input_shape=im_shape)(inputs_cnn)
    conv1_1=BatchNormalization()(conv1_1)
    pool1=MaxPool1D(pool_size=(3), strides=(2), padding="same")(conv1_1)
    conv2_1=Convolution1D(64, (3), activation='relu', input_shape=im_shape)(pool1)
    conv2_1=BatchNormalization()(conv2_1)
    pool2=MaxPool1D(pool_size=(2), strides=(2), padding="same")(conv2_1)
    conv3_1=Convolution1D(64, (3), activation='relu', input_shape=im_shape)(pool2)
    conv3_1=BatchNormalization()(conv3_1)
    pool3=MaxPool1D(pool_size=(2), strides=(2), padding="same")(conv3_1)
    flatten=Flatten()(pool3)
    dense_end1 = Dense(512, activation='relu')(flatten)
    main_output = Dense(NumberOfCodes, activation='softmax', name='main_output')(dense_end1)


    model = Model(inputs= inputs_cnn, outputs=main_output)
    model.compile(optimizer='adam',
                    loss=tf.keras.losses.CategoricalCrossentropy,
                    )

    # history=model.fit(X_train, y_train,
    #                   epochs=40,callbacks=callbacks,
    #                   batch_size=32,
    #                   validation_data=(X_test,y_test))

    feature_model = Model(inputs= inputs_cnn, outputs= dense_end1)
    return model, feature_model
