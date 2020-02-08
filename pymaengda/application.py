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
        self.data_dir = os.path.dirname(os.path.abspath(__file__)) + '/../data'
        self.data_csv = '/test.csv'
        self.data_file = self.data_dir + self.data_csv
        self.reader = data.Data()
        self.arguments = arguments.Arguments()
        self.args = self.arguments.parse_args()


    def read_data(self, infile, *args, **kwargs):
        data = self.reader.read_data(infile, *args,
                index_col=0, **kwargs)

        return data


    def write_data(self, outfile, data, *args, **kwargs):
        return self.reader.write_data(outfile + '.out',
                data, *args, **kwargs)


    def display(self):
        '''Parse arguments for specifiers such as limit, order, etc
        Read data from disk
        Format data, if necessary
        Display data'''
        data = self.read_data(self.data_file)

        print('Displaying all records...')
        print(data)


    def edit(self):
        '''This would make sense to combine delete then create to simplify
        the function. Need to think through how we call these functions.'''
        data = self.read_data(self.data_file)
        write = self.write_data(self.data_file, data)


    def create(self):
        '''Parse arguments for data to be written (e.g. strain, amount)
        Determine missing data -- timestamp
        Create row to be appended
        Append row to data file on disk'''
        data = self.read_data(self.data_file)
        write = self.write_data(self.data_file, data, mode='w')
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
        elif self.args.mode == 'burn':
            self.create()
            self.display()
        elif self.args.mode == 'rm':
            self.delete()
            self.display()
        elif self.args.mode == 'stats':
            print('statistics')
        else:
            print('Unknown mode')
