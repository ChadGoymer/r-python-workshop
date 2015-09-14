
import sys
import pandas as pd


def aggregate_csv(fname_list):
    """ Aggregate CSVs to a single data frame. """

    # Preallocate list to hold dataframes
    df_list = []

    for fname in fname_list:
        # Read csv into dataframe
        df = pd.read_csv(fname)
        df_list.append(df)

    # Concatenate all data frames row-wise
    all_dfs = pd.concat(df_list, axis=0)

    return all_dfs


if __name__ == '__main__':

    # input file names are listed first
    fname_list = sys.argv[1:-1]
    # Last argument is the output file destination
    output_file = sys.argv[-1]

    # Run aggregate function
    all_dfs = aggregate_csv(fname_list)

    # Write to csv
    # Setting quoting = 1 means quote all fields in the csv. 
    # This is necessary for R compatibility. 
    all_dfs.to_csv(output_file, index=False, quoting=1)
