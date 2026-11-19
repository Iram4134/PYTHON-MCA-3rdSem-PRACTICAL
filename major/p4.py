
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)

marks = np.array([20, 30, 40, 50, 60, 70, 80, 90])

# Create model
model = LinearRegression()

# Train model
model.fit(hours, marks)

# Predict marks
predicted = model.predict(hours)

print("Predicted Marks:")
print(predicted)

# Predict marks for different study hours
new_hours = np.array([[3], [5], [9], [10]])

new_marks = model.predict(new_hours)

for i in range(len(new_hours)):
    print("Hours:", new_hours[i][0],
          "Predicted Marks:", new_marks[i])

# Plot graph
plt.scatter(hours, marks, label="Actual Marks")

plt.plot(hours, predicted, color='red',
         label="Regression Line")

plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.legend()

plt.show()
