import matplotlib.pyplot as plt

# Funnel data
stages = ["Awareness", "Interest", "Consideration", "Purchase"]
users = [1000, 700, 400, 150]

# -------------------------
#  PIE CHART
# -------------------------
plt.figure()
plt.pie(users, labels=stages, autopct='%1.1f%%')
plt.title("User Distribution in Marketing Funnel")
plt.show()

# -------------------------
#  STATISTICAL ANALYSIS
# -------------------------

# Total users
total_users = sum(users)

# Average users
avg_users = total_users / len(users)

# Maximum and minimum
max_users = max(users)
min_users = min(users)

# Drop-off calculation
drop_off = []
for i in range(1, len(users)):
    drop_off.append(users[i-1] - users[i])

# Print results
print("\n Statistical Analysis:")
print("Total Users:", total_users)
print("Average Users:", avg_users)
print("Highest Users:", max_users)
print("Lowest Users:", min_users)
print("Drop-offs between stages:", drop_off)
