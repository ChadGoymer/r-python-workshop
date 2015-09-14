
import json 
import datetime as dt
import pandas as pd 
import sys


def process_json(fname):
    """ Extract JSON fields and clean the date field. """

    # Load the file using json module
    json_obj = json.load(open(fname))

    # Extract the records
    records = json_obj["history"]["observations"]

    # Replace "date" and "utcdate" fields of each record with a 
    # time formatted string
    # Format = %Y-%m-%d %H:%M:%S 
    for rec in records:
        rec = clean_date(rec)

    return records


def clean_date(record):
    """ Replace a date field with a string formatted date """

    for date_field in ['date', 'utcdate']:
            
        x = record[date_field]

        # Pass as a datetime object. 
        # Note datetime expects input to be integers 
        date_obj = dt.datetime(
            int(x['year']),
            int(x['mon']),
            int(x['mday']),
            int(x['hour']),
            int(x['min']),
        )

        # Format date to new string
        record[date_field] = date_obj.strftime('%Y-%m-%d %H:%M:%S')

    return record


def json_to_df(json_records, col_names):
    """ Convert JSON To DataFrame. """

    # Convert to a dataframe
    df = pd.DataFrame(json_records)

    # Filter to only keep specific column names
    df = df[col_names]

    return df


if __name__ == '__main__':

    # Columns of the json records to keep in the csv
    col_names = ['date', 'tempm', 'wspdm', 'hum', 'pressurem']
    
    # input path is first argument 
    input_path = sys.argv[1]
    # output path is first argument
    output_path = sys.argv[2]

    # Fetch the weather data
    processed_json = process_json(input_path)

    # JSON to DataFrame
    df = json_to_df(processed_json, col_names)

    # Write to a csv file
    df.to_csv(output_path, index=False)

