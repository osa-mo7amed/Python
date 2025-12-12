import json
import requests
import sys
import random

if len(sys.argv) != 2:
    sys.exit()
S =int(input("Songs limit: "))
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={S}&term=" + sys.argv[1] ) # Fetch data from iTunes API
data = response.json() # .JSON() method to parse JSON response
results = data.get("results", [])
random.shuffle(results) # Shuffle the results to get random songs

for result in results:
    print(f"{result['trackName']} by {result['artistName']}")
