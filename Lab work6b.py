import pandas as pd
import matplotlib.pyplot as plt

# 1. Load scores.csv into a DataFrame
df = pd.read_csv("scores.csv")

# Display the data
print(df)

# 2. Scatter plot of student scores
plt.figure(figsize=(8, 10))

plt.scatter(df.index, df["math"], label="Math")
plt.scatter(df.index, df["python"], label="Python")
plt.scatter(df.index, df["db"], label="Database")

plt.xlabel("Student")
plt.ylabel("Score")
plt.title("Student Scores")
plt.legend()
plt.grid(True)

plt.savefig("scattered.png")
plt.show()


# 3. Histograms of each course on separate subplots
fig, axes = plt.subplots(1, 3, figsize=(13, 5))

axes[0].hist(df["math"], bins=10, edgecolor="black")
axes[0].set_title("Math Scores")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Frequency")

axes[1].hist(df["python"], bins=10, edgecolor="black")
axes[1].set_title("Python Scores")
axes[1].set_xlabel("Score")
axes[1].set_ylabel("Frequency")

axes[2].hist(df["db"], bins=10, edgecolor="black")
axes[2].set_title("Database Scores")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("histo.png")
plt.show()


# 4. A single box plot for all courses
plt.figure(figsize=(8, 6))

df[["math", "python", "db"]].plot(
    kind="box",
    ax=plt.gca()
)

plt.title("Score Distribution by Course")
plt.ylabel("Score")
plt.grid(True)

plt.savefig("box.png")
plt.show()
import os
import pandas as pd

# Xác định đường dẫn thư mục chứa file script
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "scores.csv")

df = pd.read_csv(csv_path)