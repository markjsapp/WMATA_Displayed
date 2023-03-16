import http.client, urllib.request, urllib.parse, urllib.error, json, time, requests, os, platform
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WMATA_API_KEY")

def clear_console():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

def jprint(obj):
    if isinstance(obj, str):
        obj = json.loads(obj)
    formatted_json = json.dumps(obj, indent=4)
    # Prints formatted
    #print(formatted_json)
    # Returns as a dict
    return obj

def get_arrival_info(location_code, api_key):
    headers = {
        'api_key': api_key,
    }

    try:
        url = f'https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{location_code}'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def print_train_status(json_response):
    if json_response['Min'] == 'BRD' or json_response['Min'] == 'ARR':
        color_code = "\033[31m"  # Red
    elif json_response['Min'].isdigit() and int(json_response['Min']) < 10:
        color_code = "\033[38;2;255;165;0m"  # Custom orange color (RGB: 255, 165, 0)
    else:
        color_code = "\033[32m"  # Green

    reset_code = "\033[0m"

    # Set the train line color based on the train line
    if json_response['Line'] == "OR":
        train_line_color = "\033[38;2;255;165;0m"  # Custom orange color (RGB: 255, 165, 0)
    elif json_response['Line'] == "SV":
        train_line_color = "\033[37m"  # Light Gray (Silver)
    else:
        train_line_color = reset_code

    print(f"\rTrain Line: {train_line_color}{json_response['Line']}{reset_code}")
    print(f"\rArrival Station: {json_response['LocationName']}")
    print(f"\rDestination Station: {json_response['DestinationName']}")

    if json_response['Min'] == 'BRD':
        print(f"\r{color_code}Train is Currently Boarding{reset_code}                  ", end='')
    elif json_response['Min'] == 'ARR':
        print(f"\r{color_code}Train is Arriving{reset_code}                  ", end='')
    else:
        print(f"\rArriving in: {color_code}{json_response['Min']} minutes{reset_code}                  ", end='')

def main():
    api_key = os.getenv("WMATA_API_KEY")
    if not api_key:
        print("Please set the WMATA_API_KEY environment variable.")
        return

    location_code = 'K01'
    data = get_arrival_info(location_code, api_key)
    if data:
        trains = jprint(data)['Trains']
        if trains:
            clear_console()  # Clear console before printing train status
            for train in trains:
                print_train_status(train)

            while True:
                data = get_arrival_info(location_code, api_key)
                if data:
                    trains = jprint(data)['Trains']
                    if trains:
                        clear_console()  # Clear console before printing train status
                        for train in trains:
                            print_train_status(train)
                    else:
                        print("No train data available")
                time.sleep(30)
        else:
            print("No train data available")

if __name__ == '__main__':
    main()

# Relevant Station Codes
#Virginia Square: K03
#Ballston-MU: K04
#Clarendon: K02
#Court House: K01
#Rosslyn: C05
#Pentagon City: C08