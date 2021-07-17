import numpy as np
#import keras
import tensorflow as tf
from tensorflow import keras
#from keras.metrics import categorical_accuracy, top_k_categorical_accuracy
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.callbacks import ReduceLROnPlateau, ModelCheckpoint
from tensorflow.python.keras.wrappers.scikit_learn import KerasClassifier
#from sklearn.model_selection import GridSearchCV
import itertools
#from keras.preprocessing import image
#from tensorflow.python.keras.applications.mobilenet import MobileNet

graph = tf.get_default_graph()
#Create a MobileNet model
mobile = tf.keras.applications.mobilenet.MobileNet()

# Modify the model
# Choose the 6th layer from the last
x = mobile.layers[-6].output

# Add a dropout and dense layer for predictions
x = Dropout(0.25)(x)
predictions = Dense(7, activation='softmax')(x)

# Create a new model with the new outputs
model = Model(inputs=mobile.input, outputs=predictions)

# Prevent everything except the last 23 layers from being trained
for layer in model.layers[:-23]:
  layer.trainable = False

# Define Top2 and Top3 Accuracy

'''def top_3_accuracy(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=3)

def top_2_accuracy(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=2)'''

# Add weights to make the model more sensitive to melanoma
class_weights={
    0: 1.0,  # akiec
    1: 1.0,  # bcc
    2: 1.0,  # bkl
    3: 1.0,  # df
    4: 1.0,  # mel
    5: 1.0,  # nv
    6: 1.0,  # vasc
}

# Compile the model
model.compile(Adam(lr=0.0001), loss='categorical_crossentropy')

model.load_weights('model.h5')

#model = keras.models.load_model('model.h5')


def diseasePredictor(path):
    global graph
    # predicting images
    img = tf.keras.preprocessing.image.load_img(path, target_size=(224, 224))
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    labels = ['Actinic keratoses', 'Basal cell carcinoma', 'Benign keratosis', 'Dermatofibrom', 'Melanoma','Melanocytic nevi', 'Vascular lesions']

    images = np.vstack([x])
    
    with graph.as_default():
        classes = model.predict(images)
    return labels[list(classes[0]).index(max(list(classes[0])))]

#print(diseasePredictor('test2.jpeg'))
    
