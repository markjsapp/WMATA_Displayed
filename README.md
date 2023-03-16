# WMATA_Displayed
WMATA Train Tracker is a console-based application that uses WMATA's public API to display real-time train arrival information for a specified metro station. The application updates wait times at regular intervals, providing users with up-to-date information on train arrivals.
Features

- Displays train line, arrival station, destination station, and wait time for each train
- Color-coded output for easier readability
- Updates train arrival information every 30 seconds
- Utilizes WMATA's public API for accurate, real-time data
- Customizable station codes for tracking trains at different metro stations

## Installation

1. Clone the repository or download the source code.
    
        git clone https://github.com/yourusername/wmata-train-tracker.git

2. Navigate to the project directory.

        cd wmata-train-tracker

3. Install the required Python packages.

        pip install -r requirements.txt

4. Set up an environment variable WMATA_API_KEY with your WMATA API key.
- For Windows:

        setx WMATA_API_KEY "your_api_key"

- For Linux and macOS:

        export WMATA_API_KEY="your_api_key"

## Usage

Run the script.

       python main_display.py

The script will display train arrival information for the specified station (default is Court House).

To track a different station, update the location_code variable in the main function with the desired station code.

python

      location_code = 'K01'  # Replace 'K01' with your desired station code

## Relevant NOVA Station Codes

- Virginia Square: K03
- Ballston-MU: K04
- Clarendon: K02
- Court House: K01
- Rosslyn: C05
- Pentagon City: C08

## License

This project is licensed under the MIT License - see the LICENSE file for details.
