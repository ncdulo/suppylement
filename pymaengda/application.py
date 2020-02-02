import arguments
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
        self.arguments = arguments.Arguments()
        self.args = self.arguments.parse_args()


    def display(self, data):
        i = 1
        for row in data:
            print(f"-------- {i}")
            print(f"{row['amount']}g of {row['strain']}")
            print(f"on {row['date']}")
        print(f'Total rows: {len(data)}')


    def run(self):
        data = self.reader.read_data('../data/test.csv')

        runlevel = 1
        while runlevel > 0:
            '''Main program logic loop. Parse the values given on the command
            line and execute the desired functions. In many cases, this will
            only loop once. Certain cases such as updating a row will result
            in the loop repeating to display the updated row.

            Runlevels:
              0 - quit
              1 - display
              2 - edit
              3 - create
              4 - delete
              8 - statistics'''
            if runlevel == 0:
                print('quit')
                break
            elif runlevel == 1:
                print('display')
                self.display(data)
            elif runlevel == 2:
                print('edit')
            elif runlevel == 3:
                print('create')
            elif runlevel == 4:
                print('delete')
            elif runlevel == 8:
                print('statistics')
            #choice = input('Press x<Ret> to quit\n> ').lower()
            #if choice == 'x':
            #    runlevel = 0
            #runlevel -= 1
            runlevel = 0
