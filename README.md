# Rocket Data Plotter for SEDS UCSD

![GitHub](https://img.shields.io/github/license/dmmontoto/Rocket-Data-Plotter)

## Description

The Rocket Data Visualization Tool is a Python-based project designed to facilitate the visualization of cold flow or hot fire data from rocket experiments. This tool allows users to import data from CSV files, plot essential parameters (such as pressure and temperature) against time, and customize the resulting visualization with a user-defined title. Whether you're an engineer, researcher, or enthusiast, this project simplifies the process of gaining insights from your rocket data.

## Table of Contents 

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)
- [Badges](#badges)
- [Tests](#tests)
- [Questions](#questions)

## Installation

For installation, please download python from the web in order to run the program locally. Additionally, please use the following commands to install pandas, matplotlib, and sys: `python3 -m pip install pandas matplotlib sys`. Please ensure that the version of python you have is reciprocated by the first word. For reference, the version used in development has `python3` for calling commands instead of `python`. 

## Usage

Once you have installed, feel free to test the program with the given static CSV files. By using the command `python3 plot-data.py <csv_file>` with the desired CSV file in mind, the user will be prompted to enter a title for the plot. Inpt the desired title and press enter. Then, the tool will generate a line plot that illustrates the changes in pressure and temperature over time, with the specified title. 

## Credits

David Montoto

## License

[Unlicensed](LICENSE)

## Badges

![Languages](https://img.shields.io/github/languages/top/dmmontoto/Rocket-Data-Plotter)

## Tests

N/A