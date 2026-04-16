import matplotlib.pyplot as plt

# Simple Data
stages = ["Awareness", "Interest", "Consideration", "Purchase"]
users = [1000, 700, 400, 150]

# -------- Basic Info --------
print("Total Users:", sum(users))
print("Average Users:", sum(users)/len(users))
print("Highest Users:", max(users))
print("Lowest Users:", min(users))

# -------- Graph 1: Bar Chart --------
plt.figure()
plt.bar(stages, users)
plt.title("Users in Marketing Funnel")
plt.xlabel("Stages")
plt.ylabel("Number of Users")
plt.show()

# -------- Graph 2: Pie Chart --------
plt.figure()
plt.pie(users, labels=stages)
plt.title("User Distribution")
plt.show()
