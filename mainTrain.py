import cv2
import argparse
from pathlib import Path
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import normalize
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.utils import to_categorical



def main():
    parser = argparse.ArgumentParser(description="Train the educational CNN on a local dataset.")
    parser.add_argument("--dataset", type=Path, default=Path(__file__).resolve().parent / "datasets")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "ml/brain-tumor-classification/models/BrainTumor9EpochsCategorical.h5")
    args = parser.parse_args()
    for label_dir in ("no", "yes"):
        if not (args.dataset / label_dir).is_dir():
            parser.error("Dataset missing: provide a directory with no/ and yes/ JPEG images.")
    if args.output.exists():
        parser.error("Output already exists. Choose another --output to preserve trained weights.")
    image_directory = args.dataset
    no_tumor_images = list((image_directory / "no").iterdir())
    yes_tumor_images = list((image_directory / "yes").iterdir())
    dataset=[]
    label=[]

    INPUT_SIZE=64
    # print(no_tumor_images)

    # path='no0.jpg'

    # print(path.split('.')[1])

    for i , image_name in enumerate(no_tumor_images):
        if image_name.is_file() and image_name.suffix.lower() in {'.jpg', '.jpeg'}:
            image=cv2.imread(str(image_name))
            if image is None:
                parser.error('Dataset contains an unreadable JPEG image.')
            image=Image.fromarray(image,'RGB')
            image=image.resize((INPUT_SIZE,INPUT_SIZE))
            dataset.append(np.array(image))
            label.append(0)

    for i , image_name in enumerate(yes_tumor_images):
        if image_name.is_file() and image_name.suffix.lower() in {'.jpg', '.jpeg'}:
            image=cv2.imread(str(image_name))
            if image is None:
                parser.error('Dataset contains an unreadable JPEG image.')
            image=Image.fromarray(image, 'RGB')
            image=image.resize((INPUT_SIZE,INPUT_SIZE))
            dataset.append(np.array(image))
            label.append(1)

    if len(dataset) < 5 or set(label) != {0, 1}:
        parser.error('Provide at least five readable images, including both classes.')

    dataset=np.array(dataset)
    label=np.array(label)


    x_train, x_test, y_train, y_test=train_test_split(dataset, label, test_size=0.2, random_state=0)

    # Reshape = (n, image_width, image_height, n_channel)

    # print(x_train.shape)
    # print(y_train.shape)

    # print(x_test.shape)
    # print(y_test.shape)

    x_train=normalize(x_train, axis=1)
    x_test=normalize(x_test, axis=1)

    y_train=to_categorical(y_train , num_classes=2)
    y_test=to_categorical(y_test , num_classes=2)



    # Model Building
    # 64,64,3

    model=Sequential()

    model.add(Conv2D(32, (3,3), input_shape=(INPUT_SIZE, INPUT_SIZE, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(32, (3,3), kernel_initializer='he_uniform'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))


    model.add(Conv2D(64, (3,3), kernel_initializer='he_uniform'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2))
    model.add(Activation('softmax'))


    # Binary CrossEntropy= 1, sigmoid
    # Categorical Cross Entryopy= 2 , softmax

    model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])


    model.fit(x_train, y_train, 
    batch_size=16, 
    verbose=1, epochs=9, 
    validation_data=(x_test, y_test),
    shuffle=False)


    args.output.parent.mkdir(parents=True, exist_ok=True)
    model.save(args.output)








if __name__ == "__main__":
    main()
