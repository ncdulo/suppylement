import pandas as pd


class Data():
    def __init__(self, data_file, write_file=None):
        self._data = None
        self.read_file = data_file
        if write_file is None:
            self.write_file = data_file
        else:
            self.write_file = write_file

    def read_data(self, *args, **kwargs):
        self._data = pd.read_csv(self.read_file, *args, **kwargs)

        if self._data is None:
            print(f'Error reading {infile}')
        return self._data

    def write_data(self, *args, **kwargs):
        if self._data is None:
            print('Error no data to write')
            return False
        self._data.to_csv(self.write_file, *args, **kwargs)

