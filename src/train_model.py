from tensorflow import keras
import tensorflow as tf
import numpy as np
import pandas as pd
from datetime import datetime
from matplotlib.pyplot as plt
import os

os.makedirs("logs",exist_ok=True)

print(f"load mnist dataset")
(x_train,y_train),(x_test,y_test)=keras.datasets.mnist.load_data()
x_train=x_train.astype("float32")/255.0
x_test=x_test.astype("float32")/255.0

x_train=x_train.reshape(-1,28,28,1)
x_test=x_test.reshape(-1,28,28,1)
