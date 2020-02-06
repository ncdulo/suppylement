import pandas as pd


class Data():
    def __init__(self):
        self._data = None

    def read_data(self, infile, *args, **kwargs):
        self._data = pd.read_csv(infile, *args, **kwargs)

        if self._data is None:
            print(f'Error reading {infile}')
        return self._data

    def write_data(self, outfile, *args, **kwargs):
        if self._data is None:
            print('Error no data to write')
            return False
        self._data.to_csv(outfile, *args, **kwargs)

