import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Historical data
years = np.array([2020, 2021, 2022, 2023, 2024, 2025]).reshape(-1, 1)
temperature = np.array([27.2, 27.4, 27.6, 27.8, 28.0, 28.2])

# Train model
model = LinearRegression()
model.fit(years, temperature)

# Future years
future_years = np.array([2026, 2027, 2028, 2029, 2030]).reshape(-1, 1)
predicted_temperature = model.predict(future_years)

# Plot historical data
plt.scatter(years, temperature, color="blue", label="Actual")

# Plot prediction
plt.plot(
    future_years,
    predicted_temperature,
    color="red",
    marker="o",
    label="Predicted"
)

plt.title("Environmental Temperature Prediction")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()