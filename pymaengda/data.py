import pandas as pd


class Data():
    def __init__(self):
        pass

    def read_data(self, infile):
        data = pd.read_csv(infile, index_col=0, parse_dates=[[0,1]])

        if data is None:
            print(f'Error reading {infile}')
        return data
