import pandas as pd


class Data():
    def __init__(self):
        pass

    def read_data(self, infile, *args, **kwargs):
        data = pd.read_csv(infile, *args, **kwargs)

        if data is None:
            print(f'Error reading {infile}')
        return data

    def write_data(self, outfile, data, *args, **kwargs):
        if data is None:
            print('Error no data to write')
            return False
        data.to_csv(outfile, *args, **kwargs)

