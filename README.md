# Stock-News-AlertPython Stock Alert Program
## Overview
The Python Stock Alert Program is a tool designed to monitor stock price movements and notify you when a stock price changes by a specified percentage. It also provides relevant news headlines and brief descriptions explaining the price changes. This program helps you stay informed and make timely investment decisions.

## Features

**Customizable Alerts:** Set a percentage threshold for price changes (default is 5%). Receive notifications when the stock price increases or decreases by this amount.

**News Integration:** Fetches and sends the latest news headlines and brief descriptions related to the stock's price movement.

**Phone Notifications:** Alerts are sent directly to your phone for convenience and real-time updates.

## Prerequisites
Before running the program, ensure you have the following:

Python 3.x installed on your machine.
Required Python libraries: requests, pandas, twilio (or any other notification library you prefer).
Installation

### Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/stock-alert-program.git
cd stock-alert-program
Install Dependencies:
Create a virtual environment (optional but recommended) and install the required libraries:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

## Program Flow:

The script fetches stock data at regular intervals.
It checks for price changes against the defined thresholds.
Sends notifications if the stock price change meets or exceeds the specified percentage.
Retrieves and sends relevant news headlines and descriptions.
Customization

**Change Alert Percentage:** Modify the percentage_change value in for each stock.

**Add More Stocks:** Include additional stock symbols and alert thresholds in the config.json file.

**Notification Settings:** Adjust notification settings and methods as needed.

## Troubleshooting
**Ensure API Access:** Make sure you have valid API keys and permissions for stock data and news sources.

**Check Dependencies:** Verify that all required Python libraries are installed correctly.

**Configuration Errors:** Double-check the config.json file for correct formatting and valid values.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Inspired by various stock tracking tools and financial APIs.
Thanks to the developers of the libraries and APIs used in this project.
Contact
For questions or suggestions, feel free to reach out:

Email: paramvirgrewal232@gmail.com

Happy investing! 📈📉
