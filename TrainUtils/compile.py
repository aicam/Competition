from .config import *
from .model import *


def getNewModel(base_model):
    new_dense_layer = Dense(LastLayerDense, activation=LastLayerActivationFunction)(base_model)
    return Dense(1, activation='softmax')(new_dense_layer)




