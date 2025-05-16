# Euro to Pound Transfer Fee Converter ⚽

A simple Python command-line tool that converts an amount in Euros (€) to British Pounds (£) using live exchange rates fetched from a public API.

## Features

- Fetches the latest EUR to GBP exchange rate automatically.
- Converts user-entered Euro amounts to Pounds.
- Handles invalid inputs and negative amounts gracefully.
- Provides a clear and user-friendly console interface.

## Requirements

- Python 3.6+
- `requests` library (for API calls)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/euro-to-pound-converter.git
cd euro-to-pound-converter
Install required packages:


pip install requests
Usage
Run the program with:


python main.py
You will be prompted to enter an amount in Euros. The program will display the equivalent amount in British Pounds using the current exchange rate.

File Structure
main.py: Main script to run the converter.

exchange_rate_api.py: Module to fetch live exchange rates from the API.

README.md: This file.

Notes
The program relies on a free exchange rate API. If the API changes or requires an access key, you may need to update the exchange_rate_api.py accordingly.

Make sure you have an active internet connection to fetch live exchange rates.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Created by Ashley Toomey
