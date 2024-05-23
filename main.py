from keras.preprocessing.image import ImageDataGenerator
from  keras.layers import Dense,Input,Dropout,GlobalAveragePooling2D,Flatten,Conv2D,BatchNormalization,Activation,MaxPooling2D
from keras.models import Model,Sequential
from keras.optimizers import adam_v2,sgd_experimental, rmsprop_v2