import argparse


class Arguments():
    def __init__(self):
        print('Arguments.__init__')
        self.parser = argparse.ArgumentParser()

    def parse_args(self):
        print('parse_args')
        self.parser.add_argument(
                '-r', '--runlevel',
                type=int,
                help='runlevel to start in',
                dest='runlevel')
        self.parser.add_argument(
                '-a', '--amount',
                type=float,
                help='amount (in grams) of the burn',
                dest='amount')
        self.parser.add_argument(
                '-s', '--strain',
                type=str,
                help='strain name',
                dest='strain')
        self.args = self.parser.parse_args()
        print(f"self.args.runlevel='{self.args.runlevel}'")
        print(f"self.args.amount='{self.args.amount}', self.args.strain='{self.args.strain}'")

        return self.args
