import http.client, urllib.request, urllib.parse, urllib.error, json, time

# Utility method to help my dumbass debug, it formats the response JSON data
def jprint(obj):
    formatted_json = json.dumps(json.loads(obj), indent=4)
    # Prints formatted
    #print(formatted_json)
    # Returns as a dict
    return json.loads(obj)


def main():
    json_response = jprint(data)
    # Accessing elements example
    print('Arrival Station: ' + json_response['Trains'][0]['LocationName'])
    print('Destination Station: ' + json_response['Trains'][0]['DestinationName'])
    if(json_response['Trains'][0]['Min'] == 'BRD'):
        print('Train is Currently Boarding')
    elif(json_response['Trains'][0]['Min'] == 'ARR'):
        print('Train is Arriving')
    else: 
        print('Arriving in: ' + json_response['Trains'][0]['Min'] + ' minutes')

if __name__ == '__main__':
# Everything below is boiler plate for the rail prediction endpoint
# Standard subscription limits a user to 50,000 API calls a day 
# So we're gonna loop this thing to update every thirty seconds
    while(True): 
        # Request headers
        headers = {
            'api_key': '618d7761e61f43c18c13ce9f47a83b9b',
            }

        params = urllib.parse.urlencode({
        })

        try:
            conn = http.client.HTTPSConnection('api.wmata.com')
            conn.request("GET", "/StationPrediction.svc/json/GetPrediction/K01?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            #print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

        # Now we run our thing 
        main()
        time.sleep(30)

# Relevant Station Codes
#Virginia Square: K03
#Ballston-MU: K04
#Clarendon: K02
#Court House: K01
#Rosslyn: C05
#Pentagon City: C08