import http.client, urllib.request, urllib.parse, urllib.error, json, time

# Utility method to help my dumbass debug, it formats the response JSON data
def jprint(obj):
    formatted_json = json.dumps(json.loads(obj), indent=4)
    # Prints formatted
    #print(formatted_json)
    # Returns as a dict
    return json.loads(obj)


def get_arrival_info(location_code):
    # Everything below is boiler plate for the rail prediction endpoint
    # We pass in the 
    headers = {
            'api_key': '618d7761e61f43c18c13ce9f47a83b9b',
            }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", f'/StationPrediction.svc/json/GetPrediction/{location_code}?%s' % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        return print("[Errno {0}] {1}".format(e.errno, e.strerror))

def main():
    # I only care about the Court House metro
    location_code = 'K01'
    return_data = get_arrival_info(location_code)
    json_response = jprint(return_data)['Trains'][0]
    print('\rArrival Station: ' + json_response['LocationName'])
    print('\rDestination Station: ' + json_response['DestinationName'])

    while(True):
        return_data = get_arrival_info(location_code)
        json_response = jprint(return_data)['Trains'][0]
        if(json_response['Min'] == 'BRD'):
            print('\rTrain is Currently Boarding                  ', end='')
        elif(json_response['Min'] == 'ARR'):
            print('\rTrain is Arriving                  ', end='')
        else: 
            print('\rArriving in: ' + json_response['Min'] + ' minutes                  ', end='')
        time.sleep(30)

if __name__ == '__main__':
    main()

# Relevant Station Codes
#Virginia Square: K03
#Ballston-MU: K04
#Clarendon: K02
#Court House: K01
#Rosslyn: C05
#Pentagon City: C08