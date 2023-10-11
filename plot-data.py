import pandas as pd
import matplotlib.pyplot as plt
import sys

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
    if len(sys.argv) != 2:
        print("Usage: python3 plot-data.py <csv_file>")
    else:
        csv_file = sys.argv[1]
        title = input("Enter a title for the plot: ")
        plot_data(csv_file, title)
