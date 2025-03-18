import sys,requests


# Send request to API and return response
def getResp(url):
    headers = {
        "Host": "asn-lookup.p.rapidapi.com",
        "X-Rapidapi-Host": "asn-lookup.p.rapidapi.com",
        "X-Rapidapi-Key": "YOUR_API_KEY" # placeholder for api key of asn-lookup api
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Return JSON response
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None


# available options or flags in this tool
options = [
    "-ip",  # flag for ip address
    "-r",   # flag for cidr range
    "-a"    # flag for asn
]

# defining the api endpoint
endpoint = "https://asn-lookup.p.rapidapi.com/api?"

opt = None
qvalue = None

# checking whether there is a minimum of two parameters excluding the program call
try:
    if len(sys.argv) < 3:
        raise ValueError("syntax error")
except ValueError as e:
    print("Error : syntax error")
    exit()


# iterating through parameters. Analyzing and validating them to know whether the parameters are valid, in right order
# and to initialize required variables from these params
for i,arg in enumerate(sys.argv[1:], start=1):
    try:
        if arg in options and opt == None and qvalue == None:
            opt = arg

        elif arg not in options and qvalue == None and opt != None:
            qvalue = arg

        else:
            raise ValueError("invalid option")

    
    except ValueError as e:
        print(f"Error : {e}")
        exit()

# creating the url according to the parameters
if opt == "-ip":
    url = endpoint + f"ip={qvalue}"
elif opt == "-r":
    url = endpoint + f"cidr={qvalue}"
elif opt == "-a":
    url = endpoint + f"asn={qvalue}"

# prints the requesting url
print(url)

# prints the response in raw json
print(getResp(url))