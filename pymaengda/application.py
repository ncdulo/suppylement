import data_reader


''' Basic program structure
Parse command line arguments. Maybe config file?
Read data file, parse into memory
Perform operation
 - Create
 - Edit
 - View
 - Delete
 - Calculate statistics
Write data to disk, if applicable
Display output'''


class Application():
    def __init__(self):
        '''This seems like a good place to parse our arguments and decide
        the best course of action. We do not read any data here as some
        argument combinations will not require any to be read (help, version
        information). '''
        self.reader = data_reader.Data_Reader()


    def run(self):
        data = self.reader.read_data('../data/test.csv')
        i = 1
        for row in data:
            print(f"-------- {i}")
            print(f"{row['amount']}g of {row['strain']}")
            print(f"on {row['date']}")

        runlevel = 5
        while runlevel > 0:
            print('Running application')
            choice = input('Press x<Ret> to quit\n> ').lower()
            if choice == 'x':
                runlevel = 0

            runlevel -= 1
