
import tensorflow as tf
import matplotlib.pyplot as plt
import time

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize data
X_train = X_train / 255.0
X_test = X_test / 255.0

# Display first image
plt.imshow(X_train[0], cmap='gray')
plt.title("Handwritten Digit")
plt.show()

# Create Deep Neural Network
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Calculate training time
start = time.time()

# Train model
model.fit(X_train, y_train, epochs=3,
          batch_size=32)

end = time.time()

print("Training Time:", end - start, "seconds")

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)

print("Test Accuracy:", accuracy * 100, "%")

# Predict one image
prediction = model.predict(X_test[:1])

print("Predicted Digit:", prediction.argmax())
print("Actual Digit:", y_test[0])
