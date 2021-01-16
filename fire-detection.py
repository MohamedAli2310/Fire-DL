import os
import numpy as np
import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Input, Dropout
from tensorflow.keras.optimizers import SGD
from playsound import playsound
import matplotlib.pyplot as plt
from PIL import Image
import cv2

train = "FIRE-SMOKE-DATASET/Train"

train_gen = ImageDataGenerator(
    rescale=1./255, zoom_range=0.15, horizontal_flip=True)

val = "FIRE-SMOKE-DATASET/Test"
val_gen = ImageDataGenerator(rescale=1./255)

train_generator = train_gen.flow_from_directory(
    train,
    # resize all images to (224,224)
    target_size=(224, 224),
    shuffle=True,
    # returns 2D one-hot encoded labels
    class_mode='categorical',
    batch_size=128
)

validation_generator = val_gen.flow_from_directory(
    val,
    # resize all images to (224,224)
    target_size=(224, 224),
    # returns 2D one-hot encoded labels
    class_mode='categorical',
    shuffle=True,
    batch_size=14
)


input_tensor = Input(shape=(224, 224, 3))

base_model = InceptionV3(input_tensor=input_tensor, include_top=False)

# starts with the output of an instance of InceptionV3 (pretrained)
x = base_model.output
# averages all feature maps of each category into one feature map
x = GlobalAveragePooling2D()(x)
x = Dense(2048, activation='relu')(x)
# randomly sets input units to 0 with a frequency of 0.25 at each step during
# training to prevent overfitting. Inputs not set to 0 are scaled up by 1/0.75
x = Dropout(0.25)(x)
x = Dense(1024, activation='relu')(x)
x = Dropout(0.2)(x)
predictions = Dense(2, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer='adam',
              loss='categorical_crossentropy', metrics=['acc'])


class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('val_loss') <= 0.1 and logs.get('loss') <= 0.1):
            self.model.stop_training = True

callbacks = myCallback()

history = model.fit(
    train_generator,
    # best results at 10,16,10
    steps_per_epoch=1,
    epochs=1,
    validation_data=validation_generator,
    validation_steps=1,
    callbacks=[callbacks]
)


acc_list = history.history['acc']
val_acc_list = history.history['val_acc']
loss_list = history.history['loss']
val_loss_list = history.history['val_loss']

# freezes top layers to train last layers
for layer in model.layers[:200]:
    layer.trainable = False
for layer in model.layers[200:]:
    layer.trainable = True

# momentum accelerates gradient descent and dampens oscillations.
model.compile(optimizer=SGD(lr=0.0001, momentum=0.9),
              loss='categorical_crossentropy', metrics=['acc'])

history = model.fit(
    # best results at 10,10,10
    train_generator,
    steps_per_epoch=1,
    epochs=1,
    validation_data=validation_generator,
    validation_steps=1,
    callbacks=[callbacks]
)
print(len(base_model.layers))

# summarize history for accuracy
plt.plot(acc_list + history.history['acc'])
plt.plot(val_acc_list + history.history['val_acc'])
plt.title('Model Accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(loss_list + history.history['loss'])
plt.plot(val_loss_list + history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()


video = cv2.VideoCapture(0)
i = 0
while True:
    # counter to only run the alarm at most once every 8 frames (0.5 seconds)
    if i==8:
        i=0
    ret, frame = video.read()
    # Convert the captured frame into RGB
    im = Image.fromarray(frame, 'RGB')
    # Resizing into 224x224 because we trained the model with this image size.
    im = im.resize((224, 224))
    img_array = image.img_to_array(im)
    img_array = np.expand_dims(img_array, axis=0) / 255
    probabilities = model.predict(img_array)[0]
    prediction = np.argmax(probabilities)
    if prediction == 0:
        # algorithm has to be at least 75% sure a fire exists
        if probabilities[prediction] > 0.75:
            # only play alarm once in 8 consecutive fire frames
            if i == 0:
                playsound('alarm.wav')
                print("ALARM!")
            print("FIRE: ",probabilities[prediction])
        else:
            print(probabilities[prediction])
    i+=1

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
