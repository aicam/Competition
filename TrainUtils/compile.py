from .config import *
from .model import *

import keras.backend as K

def loss_func(y_true, y_pred):
    return K.abs(y_true - y_pred)



def getNewModel(base_model):


    new_dense_layer = Dense(NewLastLayerDense1, activation=NewLastLayerActivationFunction1)(base_model.layers[-1].output)

    return Model(inputs=base_model.input, outputs=[new_dense_layer])

def compileModel(model):
    return model.compile(loss=loss_func, optimizer='adam', metrics=['MSE', 'RMSE'])


