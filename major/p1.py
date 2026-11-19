
import pandas as pd
import matplotlib.pyplot as plt

# Creating a dataset
data = {
    'Name': ['Aman', 'Riya', 'John', 'Sara', 'Ali',
             'Neha', 'Raj', 'Simran'],
    'Marks': [80, 90, 70, 85, 60, 95, 75, 88],
    'Age': [21, 22, 20, 21, 23, 22, 20, 21],
    'Department': ['MCA', 'MBA', 'MCA', 'MBA',
                   'MCA', 'MBA', 'MCA', 'MBA']
}

# Convert into DataFrame
df = pd.DataFrame(data)

# Save dataset as CSV
df.to_csv('students.csv', index=False)

# Read CSV file
df = pd.read_csv('students.csv')

# (a) Display first five records
print("First Five Records:")
print(df.head())

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# (b) Statistical operations
print("\nMean:", df['Marks'].mean())
print("Median:", df['Marks'].median())
print("Minimum:", df['Marks'].min())
print("Maximum:", df['Marks'].max())
print("Standard Deviation:", df['Marks'].std())

# (c) Count missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df['Marks'] = df['Marks'].fillna(df['Marks'].median())
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Department'] = df['Department'].fillna(
    df['Department'].mode()[0]
)

# (d) Group by Department and calculate mean
group = df.groupby('Department')['Marks'].mean()

print("\nDepartment-wise Mean:")
print(group.sort_values(ascending=False))

# (e) Filter marks above overall mean
mean_marks = df['Marks'].mean()

filtered = df[df['Marks'] > mean_marks]

print("\nStudents Above Average:")
print(filtered)

print("Number of Records:", len(filtered))

# (f) Data Visualization

# Histogram
plt.hist(df['Marks'], bins=5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Bar Chart
group.sort_values().plot(kind='bar')
plt.title("Department-wise Average Marks")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.show()

# Scatter Plot
plt.scatter(df['Age'], df['Marks'])
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()

