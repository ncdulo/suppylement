import argparse


class Arguments():
    def __init__(self):
        print('Arguments.__init__')
        self.parser = argparse.ArgumentParser(
                description='''
                Quick & easy to use kratom burn tracking software
                https://github.com/ncdulo/pymaengda
                '''
            )
        self.subparsers = self.parser.add_subparsers(
                dest='mode',
                help='modes')

    def parse_args(self):
        print('parse_args')
        self.parser.add_argument(
                '-r', '--runlevel',
                default=1,
                choices=[0,1,2,3,4,8],
                type=int,
                help='runlevel to start in',
                dest='runlevel')
        #self.parser.add_argument(
        #        '-a', '--amount',
        #        type=float,
        #        help='amount (in grams) of the burn',
        #        dest='amount')
        #self.parser.add_argument(
        #        '-s', '--strain',
        #        type=str,
        #        help='strain name',
        #        dest='strain')
        self.list_parser = self.subparsers.add_parser(
                'list', help='list burns')
        self.list_parser.add_argument(
                '--most-recent',
                dest='most_recent',
                type=int,
                default=5,
                help='display MOST_RECENT burns, default 5')
        self.edit_parser = self.subparsers.add_parser(
                'edit', help='not yet implemented')
        self.edit_parser.add_argument(
                'id',
                type=int,
                help='id of entry to edit')

        self.burn_parser = self.subparsers.add_parser(
                'burn', help='add a burn')
        self.burn_parser.add_argument(
                'amount',
                type=float,
                help='amount in grams')
        self.burn_parser.add_argument(
                'strain',
                type=str,
                help='name of strain burned')

        self.rm_parser = self.subparsers.add_parser(
                'rm',
                help='remove specific entries')
        self.rm_parser.add_argument(
                '--most-recent',
                dest='most_recent',
                type=int,
                default=1,
                help='remove MOST_RECENT entries')

        self.args = self.parser.parse_args()
        #print(f"self.args.runlevel='{self.args.runlevel}'")
        if self.args.mode == 'burn':
            print(f"self.args.amount='{self.args.amount}', self.args.strain='{self.args.strain}'")
        elif self.args.mode == 'rm':
            print(f'self.args.most_recent = {self.args.most_recent}')
        print(f'self.args.mode = {self.args.mode}')

        return self.args
