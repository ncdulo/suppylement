import datetime

import pandas as pd
import pandas.errors as pd_error
import pathlib


class Data():
    def __init__(self, data_file, write_file=None):
        self._data = None
        self.read_file = data_file
        # If the write_file argument is not specified, default to
        # using the same file for both reading and writing.
        if write_file is None:
            self.write_file = self.read_file
        else:
            self.write_file = write_file
        # Check to ensure our read file actually exists before we need it.
        if not pathlib.Path(self.read_file).exists():
            raise FileNotFoundError(f'read_file not found!\n{self.read_file}')

    def read_data(self, *args, **kwargs):
        '''Here we try reading our data from the disk and turning it into
        a Pandas DataFrame. Handle any exceptions thrown and return None to
        indicate failure. Otherwise, maintain an instance copy of the data
        and return a copy for Application to use. The instance copy of the data
        will be used for any future operations on it.

        Note: I am just realizing, we never actually check for presence of
        an instance copy of the data to return from our cache. I am deciding
        not to add that check in at this point. We *want* to be able to read
        from disk and reset our data. This way any filters we run on the data
        are not saved with it. For all operations involving write we should
        read the data, perform our operation, then re-read the data back
        to confirm. This will reset and filter or selection changes we may
        have made to our data earlier in execution.'''
        try:
            self._data = pd.read_csv(self.read_file, *args, **kwargs)
        except pd_error.ParserError as parser_error:
            print(f'Parser error!\n{parser_error}')
            return None
        except pd_error.EmptyDataError as empty_data:
            print(f'Empty data error!\n{empty_data}')
            return None
        else:
            return self._data

    # TODO: Need error checking for failed write condition
    def write_data(self, *args, **kwargs):
        if self._data is None:
            raise ValueError('Error no data to write')
        self._data.to_csv(self.write_file, *args, **kwargs)

    def new_entry(self, amount, name):
        '''This function will accept an amount and supplement name, create a
        Pandas DataFrame with it, then finally append it to self._data.
        It is up to Application to call self.write_data to save to disk. By
        returning None we indicate failure, otherwise the new row itself is
        returned for verification if desired.'''
        if not amount > 0:
            raise ValueError(\
                    f'Error: amount ({amount}) must be greater than 0')

        entry = {
                'timestamp': [datetime.datetime.now().\
                        strftime('%Y-%m-%d %H:%M:%S')],
                'amount': [amount],
                'name': [name]
            }

        try:
            # Convert our dictionary above into Pandas DataFrame
            entry_df = pd.DataFrame(data=entry)
        except (ValueError, TypeError) as error:
            print(f'Exception caught in new_entry!\n{error}')
            return None
        else:
            try:
                # Append our new DataFrame onto the existing data from disk
                self._data = self._data.append(entry_df, ignore_index=True)
                print('Entry created!')
                print(entry_df)
                # Note we do not write data. Only return as an indication of
                # success or failure. Application itself will decide when
                # to write the data, or not.
                return entry_df
            except TypeError as error:
                print(f'Exception caught in new_entry!\n{error}')
                return None

    def delete_row_by_id(self, id_to_remove, confirm=False):
        '''Remove a row as specified by it's index value. There is some
        bounds checking to ensure the ID is within the limits of the
        DataFrame. The index will also be reset so the values flow without
        gaps after removal. Following in design for other members of this
        class, we do not save any data. We only update the values and leave
        it up to Application to verify and/or save data when necessary.'''
        if 0 <= id_to_remove <= len(self._data)-1:
            print(f'Removing entry ID {id_to_remove}:')
            print(self._data.iloc[id_to_remove])
            print()
            if confirm:
                choice = input('Are you sure you want to delete this entry? '
                        "Enter 'Y' to confirm.\n > ")
                if not choice == 'Y':
                    print('Aborted')
                    return None
            # Delete the requested row and then reset our index column
            self._data = self._data.drop(self._data.index[id_to_remove])
            self._data.reset_index(drop=True, inplace=True)
            return True
        else:
            raise ValueError('Error id_to_remove out of bounds!\n'
                    f'(0 <= {id_to_remove} <= {len(self._data)-1})')
