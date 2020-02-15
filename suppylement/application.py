import arguments
import data

import os
import sys


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
    def __init__(self, args=None):
        '''This seems like a good place to parse our arguments and decide
        the best course of action. We do not read any data here as some
        argument combinations will not require any to be read (help, version
        information). '''
        data_dir = os.path.dirname(os.path.abspath(__file__)) + '/../data'
        data_csv = '/test.csv'
        data_file = data_dir + data_csv
        self.reader = data.Data(data_file, data_file + '.out')

        self.arguments = arguments.Arguments()
        # If no args provided, default to command line args
        if args is None:
            # If command line args do not include any mode, default to list
            if len(sys.argv) < 2:
                self.args = self.arguments.parse_args(['list'])
            # Command line args are long enough
            else:
                print(sys.argv[1:])
                self.args = self.arguments.parse_args(sys.argv[1:])
        # We have been given a custom argument list
        else:
            self.args = self.arguments.parse_args(args)

        self.default_read_args = {
                'index_col': 0
            }

    def display(self):
        '''Parse arguments for specifiers such as limit, order, etc
        Read data from disk
        Format data, if necessary
        Display data'''
        data = self.reader.read_data(**self.default_read_args)

        print('Displaying all records...')
        print(data)

    def edit(self):
        '''This would make sense to combine delete then create to simplify
        the function. Need to think through how we call these functions.'''
        data = self.reader.read_data(**self.default_read_args)
        self.reader.write_data()

    def create(self):
        '''Parse arguments for data to be written (e.g. strain, amount)
        Determine missing data -- timestamp
        Create row to be appended
        Append row to data file on disk'''
        data = self.reader.read_data(**self.default_read_args)
        self.reader.write_data(mode='w')
        # NOTE: In above, change mode='a' for proper operation

    def delete(self):
        pass

    def run(self):
        '''At this point, we have already created our Data instance and parsed
        arguments. We can begin branching off into different execution modes.
        Certain modes should display the data after the action has been
        performed as a sort of verification. In these cases, just call
        self.display() again.'''
        if self.args.mode == 'list':
            self.display()
        elif self.args.mode == 'edit':
            self.edit()
            self.display()
        elif self.args.mode == 'log':
            self.create()
            self.display()
        elif self.args.mode == 'rm':
            self.delete()
            self.display()
        elif self.args.mode == 'stats':
            print('statistics')
        else:
            print('Unknown mode')
