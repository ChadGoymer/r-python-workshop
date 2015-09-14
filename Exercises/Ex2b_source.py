
import requests
import time
import sys


# You will need to register for a Wunderground API key and set it below
#
API_KEY = 'Your API key here'


def get_weather(date, location):
    """ Return the json response as a Python dictionary"""

    base_url = "http://api.wunderground.com/api/{api_key}/history_{date}/q/{location}.json"

    url = base_url.format(
        api_key=API_KEY,
        date=date, 
        location=location
    )

    r = requests.get(url)

    return r.text


if __name__ == '__main__':
    
    # Modify this script to take arguments from the command line for the location 
    # and date


    # YOUR CODE HERE


    # Fetch the weather data    
    response_string = get_weather(date, location)

    # The API is rate limited at 10 requests per minutes, 
    # so include a wait here to avoid hitting this. 
    time.sleep(6)

    # Build filename out of location and date 
    filename = location.replace('/', '-') + '--' + date

    # Write to a file
    file_handle = open('data/raw/' + filename + '.json', 'w')
    file_handle.write(response_string + '\n')
    file_handle.close()
