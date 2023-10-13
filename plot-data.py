import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_data(csv_file, title):
    try:
        data = pd.read_csv(csv_file, dtype={'Time': int, 'Pressure': float, 'Temperature': float})

        # Check if the required columns 'Time', 'Pressure', and 'Temperature' exist
        required_columns = ['Time', 'Pressure', 'Temperature']
        for col in required_columns:
            if col not in data.columns:
                print(f"Error: Column '{col}' is missing in the CSV file.")
                return

        plt.plot(data['Time'], data['Pressure'], label='Pressure')
        plt.plot(data['Time'], data['Temperature'], label='Temperature')
        plt.xlabel('Time')
        plt.ylabel('Values')
        plt.title(title)
        plt.legend()
        plt.show()

    except FileNotFoundError:
        print(f"Error: The CSV file '{csv_file}' does not exist.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty or malformed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 plot-data.py <csv_file>")
    else:
        csv_file = sys.argv[1]
        title = input("Enter a title for the plot: ")
        plot_data(csv_file, title)
