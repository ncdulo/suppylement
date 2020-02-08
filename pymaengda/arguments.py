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
        self.subparsers = self.parser.add_subparsers(help='modes')

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
        self.burn_parser = self.subparsers.add_parser(
                'burn', help='Add a burn')
        self.burn_parser.add_argument(
                'amount',
                type=float,
                help='Amount in grams')
        self.burn_parser.add_argument(
                'strain',
                type=str,
                help='Name of strain burned')

        self.args = self.parser.parse_args()
        print(f"self.args.runlevel='{self.args.runlevel}'")
        print(f"self.args.amount='{self.args.amount}', self.args.strain='{self.args.strain}'")

        return self.args
