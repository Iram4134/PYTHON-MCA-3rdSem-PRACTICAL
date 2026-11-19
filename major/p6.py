
import numpy as np
import tensorflow as tf

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report

# Create dataset
X, y = make_moons(n_samples=500, noise=0.2,
                  random_state=42)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create neural network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu',
                          input_shape=(2,)),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(X_train, y_train, epochs=20, verbose=1)

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)

print("Test Loss:", loss)
print("Test Accuracy:", accuracy * 100, "%")

# Predict output
pred = model.predict(X_test)

pred = (pred > 0.5).astype(int)

# Confusion matrix
cm = confusion_matrix(y_test, pred)

print("Confusion Matrix:")
print(cm)

print("Classification Report:")
print(classification_report(y_test, pred))
