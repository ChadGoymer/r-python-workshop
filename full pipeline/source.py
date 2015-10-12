
import requests
import time
import sys

API_KEY = 'b46469619813af9c'


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
    
    # Location string is parsed as first argument 
    locations = sys.argv[1].split(',')

    # Dates are parsed as a second parameter
    dates = sys.argv[2].split(',')

    # Passing a slash as part of the parameter name will be 
    # problematic when we use it in the output path name
    locations = [x.replace('-', '/') for x in locations]

    for date in dates:
        for location in locations:

            # Fetch the weather data
            response_string = get_weather(date, location)

            # The API is rate limited
            time.sleep(6)

            # Build filename out of location and date 
            filename = location.replace('/', '-') + '--' + date

            # Write to a file
            file_handle = open('data/raw/' + filename + '.json', 'w')
            file_handle.write(response_string + '\n')
            file_handle.close()
