import arguments
import data

import os


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
        self.reader = data.Data()
        self.arguments = arguments.Arguments()
        self.args = self.arguments.parse_args()


    def display(self, data):
        print('Displaying all records...')
        print(data)


    def run(self):
        '''I think a lot of the below block, regarding custom read arguments
        and such may be better off in it's own function. I can see it being
        reused. Might it be best in the Data class though?'''
        data_dir = os.path.dirname(os.path.abspath(__file__)) + '/../data'
        data_file = '/test.csv'
        data = self.reader.read_data(data_dir + data_file,
                index_col=0)

        # Test command. Yes, it works.
        write = self.reader.write_data(data_dir + data_file + '.out', data)

        if self.args.runlevel is not None:
            runlevel = self.args.runlevel
        else:
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
                self.display(data)
                runlevel = 0
            elif runlevel == 2:
                print('edit')
                runlevel = 1
            elif runlevel == 3:
                print('create')
                runlevel = 1
            elif runlevel == 4:
                print('delete')
                runlevel = 1
            elif runlevel == 8:
                print('statistics')
                runlevel = 1
            else:
                print('Unknown runlevel')
                runlevel = 0
