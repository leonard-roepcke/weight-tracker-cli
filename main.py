print("Tracker started")
wx = input("Enter your weight: ")
with open("weights.txt", "a") as f:
    f.write(f"{wx}\n")
print("Weight recorded.")