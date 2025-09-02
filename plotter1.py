import matplotlib.pyplot as plt



print(f"data start time: {DTtime[0]}")
print(f"data end time: {DTtime[-1]}")

plt.plot(DTtime, temp1, label='Temperature 1')
plt.plot(DTtime, temp2, label='Temperature 2')
plt.xlabel('Time')

plt.ylabel('Temperature (°C)')
plt.title('Temperature Readings')
plt.legend()
plt.show()