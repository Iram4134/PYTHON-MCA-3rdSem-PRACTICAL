
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense

from sklearn.metrics import confusion_matrix
import seaborn as sns

# Load dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Reshape images
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

# Normalize data
X_train = X_train / 255.0
X_test = X_test / 255.0

# Create CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu',
           input_shape=(28, 28, 1)),

    MaxPooling2D((2, 2)),

    Flatten(),

    Dense(64, activation='relu'),

    Dense(10, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(X_train, y_train, epochs=3,
          batch_size=32)

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)

print("Test Accuracy:", accuracy * 100, "%")

# Predict test images
pred = model.predict(X_test)

pred = np.argmax(pred, axis=1)

# Confusion matrix
cm = confusion_matrix(y_test, pred)

print("Confusion Matrix:")
print(cm)

# Display confusion matrix
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')

plt.title("CNN Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
