import matplotlib.pyplot as plt

# File containing the configuration values
config_file_path = "config.txt"  # Replace with your file path

# Read the configuration values from the file
config_values = {}
with open(config_file_path, 'r') as config_file:
    for line in config_file:
        key, value = line.strip().split(' = ')
        config_values[key.strip()] = value.strip()

# Read the ratios from the file
ratios_file_path = "ratios.txt"  # Replace with your file path

ratios = []
with open(ratios_file_path, 'r') as file:
    for line in file:
        if "Pair" in line:
            ratio = float(line.split('=')[-1].strip())
            ratios.append(ratio)

# Extract epsilon from config_values
epsilon = float(config_values["epsilon"])

# Define the range
lower_bound = 1 - epsilon
upper_bound = 1 + epsilon

# Separate ratios falling within and outside the range
within_range = [ratio for ratio in ratios if lower_bound <= ratio <= upper_bound]
outside_range = [ratio for ratio in ratios if ratio < lower_bound or ratio > upper_bound]

# Calculate the percentages
total_points = len(ratios)
within_percentage = (len(within_range) / total_points) * 100
outside_percentage = (len(outside_range) / total_points) * 100

# Plotting the histogram with x-axis label containing n, d, k, and epsilon
plt.hist(within_range, bins=50, color='blue', alpha=0.5, label=f'Within Range ({within_percentage:.10f}%)')
plt.hist(outside_range, bins=50, color='red', alpha=0.5, label=f'Outside Range ({outside_percentage:.10f}%)')

plt.xlabel(f'Ratio\nn = {config_values["n"]}, d = {config_values["d"]}, k = {config_values["k"]}, epsilon = {config_values["epsilon"]}')
plt.ylabel('Frequency')
plt.title('Histogram of Ratios')

plt.legend()

# Display the plot
plt.show()

# Count and display the number of points within and outside the range
print(f"Points within range: {len(within_range)} ({within_percentage:.10f}%)")
print(f"Points outside range: {len(outside_range)} ({outside_percentage:.10f}%)")
