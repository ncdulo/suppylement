class Data_Reader():
    def __init__(self):
        print('Data_Reader.__init__')

    def read_data(self, infile):
        with open(infile) as file:
            for line in file:
                print(line)
