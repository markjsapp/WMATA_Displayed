import http.client, urllib.request, urllib.parse, urllib.error, base64, json, sys

# Utility method to help my dumbass debug, it formats the response JSON data
def jprint(obj):
    formatted_json = json.dumps(json.loads(obj), indent=4)
    print(formatted_json)

def main():
    jprint(data)

if __name__ == '__main__':
# Everything below is boiler plate for the rail prediction endpoint
    # Request headers
    headers = {
    'api_key': '618d7761e61f43c18c13ce9f47a83b9b',
    }

    params = urllib.parse.urlencode({
    })

try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/StationPrediction.svc/json/GetPrediction/all?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

# Now we run our thing 
main()