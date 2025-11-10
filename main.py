import matplotlib.pyplot as plt

is_recorde_weight = input("Do you want to record a new weight? (y/n): ").lower() == 'y'
print("Tracker started")

if is_recorde_weight:
    wx = input("Enter your weight: ")

    # Gewicht speichern
    with open("weights.txt", "a") as f:
        f.write(f"{wx}\n")
    print("Weight recorded.")

# Werte einlesen
with open("weights.txt", "r") as file:
    lines = file.readlines()

# In Zahlen umwandeln (float erlaubt z. B. 70.5)
weights = [float(line.strip()) for line in lines if line.strip()]

print("Recorded weights:", weights)
print("Average weight:", sum(weights) / len(weights) if weights else 0)
print("Last week's average:", sum(weights[-7:]) / len(weights[-7:]) if len(weights) >= 7 else "Not enough data")

# --- Statistik anzeigen ---
plt.figure(figsize=(8, 4))
plt.plot(range(1, len(weights) + 1), weights, marker='o', linestyle='-', linewidth=2)
plt.title("Weight Tracker Progress")
plt.xlabel("Entry Number (Days)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.tight_layout()
plt.show()
