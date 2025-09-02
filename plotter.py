import matplotlib.pyplot as plt
import pandas as pd
import datetime

df = pd.read_csv('data/processed_data.csv', parse_dates = ['Time'])

print(f"data start time: {df['Time'][0]}")
print(f"data end time: {df['Time'].iloc[-1]}")

plt.plot(df['Time'], df['Temperature 1 (left pan)'], label='Temperature 1 (left pan)')
plt.plot(df['Time'], df['Temperature 2 (right pan)'], label='Temperature 2 (right pan)')
plt.xlabel('Time')

plt.ylabel('Temperature (°C)')
plt.title('Temperature Readings')
plt.legend()
plt.show()
plt.savefig("temperatureplot.png", dpi=300)