import pandas as pd
import matplotlib.pyplot as plt

def plot_data(csv_file, title):
    data = pd.read_csv(csv_file)
    plt.plot(data['Time'], data['Pressure'], label='Pressure')
    plt.plot(data['Time'], data['Temperature'], label='Temperature')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title(title)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    cold_flow_csv = 'cold-flow-data.csv'
    hot_fire_csv = 'hot-fire-data.csv'

    print("Select data to plot:")
    print("1. Cold Flow Data")
    print("2. Hot Fire Data")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        plot_data(cold_flow_csv, "Cold Flow Data")
    elif choice == 2:
        plot_data(hot_fire_csv, "Hot Fire Data")
    else:
        print("Invalid choice")
