import pandas as pd


class Data():
    def __init__(self, data_file, write_file=None):
        self._data = None
        self.read_file = data_file
        if write_file is None:
            self.write_file = read_file
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
        Pandas DataFrame with it, then finally append it to self.write_file'''
        entry = {
                'timestamp': ['2020-02-15 16:20:00'],
                'amount': [amount],
                'name': [name]
            }
        # Commenting out below -- I think we may be better off letting
        # Pandas add an index to our data. May make working with things
        # easier such as selecting, and inserting like here.
        #entry_df = pd.DataFrame(data=entry, index=entry['timestamp'])
        entry_df = pd.DataFrame(data=entry)
        final_df = self._data.append(entry_df, ignore_index=True)
        print(entry_df)
        print('----')
        print(final_df)
