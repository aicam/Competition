from TrainUtils.compile import *
from TrainUtils.model import *
from TrainUtils.config import *
import numpy as np
from tensorflow import keras

model, feature_model = build_network()
print(model.summary())