
import requests
import time
import sys


# You will need to register for a Wunderground API key and set it below
#
API_KEY = 'b46469619813af9c'


def get_weather(date, location):
    """ Return the response string from the API request. """
    url = "http://api.wunderground.com/api/{api_key}/history_{date}/q/{location}.json"
    url = url.format(api_key = API_KEY, date = date, location = location)
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    
    # Location string is parsed as first argument 
    location = "UK/London"

    # Dates are parsed as a second parameter
    date = "20150701"

    # Fetch the weather data    
    response_string = get_weather(date, location)

    # Build filename out of location and date 
    filename = location.replace('/', '-') + '--' + date

    # Write to a file
    file_handle = open('R/projects/r-python-workshop/data/raw/' + filename + '.json', 'w')
    file_handle.write(response_string + '\n')
    file_handle.close()
