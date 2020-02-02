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
        pass


    def run(self):
        runlevel = 5
        while runlevel > 0:
            print('Running application')
            choice = input('Press x<Ret> to quit\n> ').lower()
            if choice == 'x':
                runlevel = 0

            runlevel -= 1
