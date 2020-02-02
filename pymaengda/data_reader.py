import csv


class Data_Reader():
    '''I think a data cache could be helpful here. Use something like _data
    to store the input, if it is None then read the file and generate it. This
    way if we need to request a second iterator there is no extra cost
    associated with the call aside from copying memory. Note that I may be
    entirely wrong about all of that. We'll figure this one out!'''
    def __init__(self):
        self._data = None

    def read_data(self, infile):
        if self._data is None:
            with open(infile) as csvfile:
                print(f"Reading data from '{infile}'")
                reader = csv.DictReader(csvfile)
                data = list(reader)
        return data
