import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models
import cv2

# Dataset Paths
base_path = "/kaggle/input/inme-veri-seti-stroke-dataset/İNME VERİSETİ/YarısmaVeriSeti_1_Oturum"
png_path = os.path.join(base_path, "PNG")
masks_path = os.path.join(base_path, "MASKS")
overlay_path = os.path.join(base_path, "OVERLAY")

# Displaying sample images
png_files = sorted(os.listdir(png_path))[:5]
mask_files = sorted(os.listdir(masks_path))[:5]
overlay_files = sorted(os.listdir(overlay_path))[:5]

fig, axes = plt.subplots(5, 3, figsize=(12, 15))
for i in range(5):
    img = cv2.imread(os.path.join(png_path, png_files[i]))
    mask = cv2.imread(os.path.join(masks_path, mask_files[i]), cv2.IMREAD_GRAYSCALE)
    overlay = cv2.imread(os.path.join(overlay_path, overlay_files[i]))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    overlay = cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB)

    axes[i, 0].imshow(img)
    axes[i, 0].set_title("Original Image")
    axes[i, 1].imshow(mask, cmap="gray")
    axes[i, 1].set_title("Mask")
    axes[i, 2].imshow(overlay)
    axes[i, 2].set_title("Overlay")

    for ax in axes[i]:
        ax.axis("off")

plt.tight_layout()
plt.show()

# Function to load images and masks
def load_images_and_masks(image_folder, mask_folder, image_size=(256, 256)):
    images, masks = [], []
    image_files = sorted(os.listdir(image_folder))
    mask_files = sorted(os.listdir(mask_folder))

    for img_file, mask_file in zip(image_files, mask_files):
        img_path = os.path.join(image_folder, img_file)
        mask_path = os.path.join(mask_folder, mask_file)

        img = Image.open(img_path).convert("L").resize(image_size)
        mask = Image.open(mask_path).convert("L").resize(image_size)

        img = np.array(img) / 255.0
        mask = (np.array(mask) / 255.0).astype(np.float32)

        images.append(np.expand_dims(img, axis=-1))
        masks.append(np.expand_dims(mask, axis=-1))

    return np.array(images), np.array(masks)

images, masks = load_images_and_masks(png_path, masks_path)
X_train, X_val, y_train, y_val = train_test_split(images, masks, test_size=0.2, random_state=42)

# GPU Configuration
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print("GPUs Available:", gpus)
    except RuntimeError as e:
        print(e)
else:
    print("No GPU found. Running on CPU.")

# U-Net Model Definition
def unet_model(input_size=(256, 256, 1)):
    inputs = tf.keras.Input(input_size)

    conv1 = layers.Conv2D(64, 3, activation="relu", padding="same")(inputs)
    conv1 = layers.Conv2D(64, 3, activation="relu", padding="same")(conv1)
    pool1 = layers.MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = layers.Conv2D(128, 3, activation="relu", padding="same")(pool1)
    conv2 = layers.Conv2D(128, 3, activation="relu", padding="same")(conv2)
    pool2 = layers.MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = layers.Conv2D(256, 3, activation="relu", padding="same")(pool2)
    conv3 = layers.Conv2D(256, 3, activation="relu", padding="same")(conv3)

    up1 = layers.UpSampling2D(size=(2, 2))(conv3)
    concat1 = layers.concatenate([conv2, up1], axis=-1)
    conv4 = layers.Conv2D(128, 3, activation="relu", padding="same")(concat1)
    conv4 = layers.Conv2D(128, 3, activation="relu", padding="same")(conv4)

    up2 = layers.UpSampling2D(size=(2, 2))(conv4)
    concat2 = layers.concatenate([conv1, up2], axis=-1)
    conv5 = layers.Conv2D(64, 3, activation="relu", padding="same")(concat2)
    conv5 = layers.Conv2D(64, 3, activation="relu", padding="same")(conv5)

    outputs = layers.Conv2D(1, 1, activation="sigmoid")(conv5)

    model = models.Model(inputs, outputs)
    return model

model = unet_model(input_size=(256, 256, 1))
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.summary()

# Model Training
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    batch_size=8,
    epochs=5,
    verbose=1
)

# Training History Visualization
def plot_training_history(history):
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(history.history["loss"], label="Training Loss")
    plt.plot(history.history["val_loss"], label="Validation Loss")
    plt.title("Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history["accuracy"], label="Training Accuracy")
    plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
    plt.title("Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()

    plt.show()

plot_training_history(history)
