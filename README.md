# ARMS Data API Tester & Explorer

## Overview

The ARMS Data API Tester & Explorer is a Python terminal application designed to interact with the Agricultural Resource Management Survey (ARMS) Data API. It provides a user-friendly interface to test various API endpoints, explore data variables, and output results in both CSV format and as browser-accessible URLs.

## Features

- **Menu-Driven Interface**: Easy-to-navigate terminal menu to access different functionalities.
- **Endpoint Testing**: Test each endpoint (`/arms/state`, `/arms/year`, `/arms/surveydata`, `/arms/category`, `/arms/report`, `/arms/variable`, `/arms/farmtype`) with various parameters.
- **Variable Exploration**: Explore and test a significant number of variables available in the `/arms/variable` endpoint.
- **Output Formats**: Outputs include CSV files for data storage and URLs for browser access.

## Setup

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Requirements**: Run `pip install -r requirements.txt` to install the necessary packages.
3. **Configuration**: Enter your API key in the `config.py` file.
4. **Run the Application**: Execute `main.py` to start the application.

## Usage

After starting the application, use the terminal menu to navigate through different endpoints. Each option in the menu corresponds to a specific endpoint of the ARMS Data API. Follow the on-screen instructions to input parameters (if required) and view the results.

## Modules

The application is structured into various modules:

- `main.py`: Entry point of the application, containing the main menu.
- `/modules`: Contains individual modules for each endpoint.
- `/utils`: Includes utility scripts for API requests, CSV writing, and URL generation.
- `config.py`: Manages configuration settings like API key and base URL.

## Contributing

Contributions to enhance the application or add new features are welcome. Please adhere to standard coding practices and ensure compatibility with existing functionalities.