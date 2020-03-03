import configparser
import pathlib


class Configuration():
    '''Configuration class maintains a dictionary of program config
    options. We first read our defaults config file, populating our
    dictionary with default values. Then we read the user config file
    and any values set within that file should over-write the defaults.'''

    def __init__(self, default_config_file, user_config_file):
        '''Set up our configparser instance. Read default values.
        Apply user values on top of default values.'''
        self.base_dir = pathlib.Path(__file__).parent.resolve()
        self.default_config_file = self.base_dir /\
                pathlib.Path(default_config_file)
        self.user_config_file = self.base_dir /\
                pathlib.Path(user_config_file)
        # TODO: Prefer USER_CONFIG_DIR from appdirs module, if it exists.

        self.parser = configparser.ConfigParser()
        # TODO: Handle errors if file does not exist.
        with open(self.default_config_file) as f:
            self.parser.read_file(f)
        self.parser.read([self.user_config_file])

        # Assemble our data file path here. This allows the config file
        # to use relative paths to the data file. It is also a shorter
        # alias for `self.config.parser.get('read_file')`.
        self.read_file = self.base_dir /\
                self.parser.get('filenames', 'read_file')
        self.write_file = self.base_dir /\
                self.parser.get('filenames', 'write_file')

        # Debug text below
        #print(self.base_dir)
        #print(self.default_config_file)
        #print(self.user_config_file)

        #for section_name in self.parser.sections():
        #    print('section:   ', section_name)
        #    print('  options: ', self.parser.options(section_name))
        #    for name, value in self.parser.items(section_name):
        #        print('  {} = {}'.format(name, value))
        #    print()
