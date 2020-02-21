import configparser
import os


class Configuration():
    '''Configuration class maintains a dictionary of program config
    options. We first read our defaults config file, populating our
    dictionary with default values. Then we read the user config file
    and any values set within that file should over-write the defaults.'''
    def __init__(self):
        '''Set up our configparser instance. Read default values.
        Apply user values on top of default values.'''
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.default_config_file = self.base_dir + '/suppylement_defaults.ini'
        self.user_config_file = self.base_dir + '/suppylement.ini'
        # TODO: Prefer USER_CONFIG_DIR from appdirs module, if it exists.

        self.parser = configparser.ConfigParser()
        # TODO: Handle errors if file does not exist.
        with open(self.default_config_file) as f:
            self.parser.read_file(f)
        self.parser.read([self.user_config_file])
        print(self.base_dir)
        print(self.default_config_file)
        print(self.user_config_file)
