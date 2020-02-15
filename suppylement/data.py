import datetime

import pandas as pd


class Data():
    def __init__(self, data_file, write_file=None):
        self._data = None
        self.read_file = data_file
        if write_file is None:
            self.write_file = self.read_file
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

    def new_entry(self, amount, name):
        '''This function will accept an amount and supplement name, create a
        Pandas DataFrame with it, then finally append it to self._data.
        It is up to Application to call self.write_data to save to disk.'''
        entry = {
                'timestamp': [datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
                'amount': [amount],
                'name': [name]
            }

        entry_df = pd.DataFrame(data=entry)
        self._data = self._data.append(entry_df, ignore_index=True)
        print('Entry added!')
        print('Full DataFrame as it would be written to disk:')
        print(self._data)
