import sys

import argparse


class Arguments():
    def __init__(self):
        print('Arguments.__init__')
        self.parser = argparse.ArgumentParser(
                description='''
                Quick & easy to use nutritional supplement tracking software
                https://github.com/ncdulo/suppylement
                '''
            )
        self.subparsers = self.parser.add_subparsers(
                dest='mode',
                help='modes')

    def parse_args(self):
        print('parse_args')

        self.list_parser = self.subparsers.add_parser(
                'list', help='list entries')
        self.list_parser.add_argument(
                '--most-recent',
                dest='most_recent',
                type=int,
                default=5,
                help='display MOST_RECENT entries, default 5')

        self.edit_parser = self.subparsers.add_parser(
                'edit', help='not yet implemented')
        self.edit_parser.add_argument(
                'id',
                type=int,
                help='id of entry to edit')

        self.log_parser = self.subparsers.add_parser(
                'log', help='log an entry')
        self.log_parser.add_argument(
                'amount',
                type=float,
                help='amount in miligrams')
        self.log_parser.add_argument(
                'name',
                type=str,
                help='name of supplement')

        self.rm_parser = self.subparsers.add_parser(
                'rm',
                help='remove specific entries')
        self.rm_parser.add_argument(
                '--most-recent',
                dest='most_recent',
                type=int,
                default=1,
                help='remove MOST_RECENT entries')

        self.stats_parser = self.subparsers.add_parser(
                'stats',
                help='display various statistics')
        self.stats_parser.add_argument(
                '--full',
                default=False,
                action='store_true',
                help='full output mode')

        # If we are not given enough arguments, provide a default of list
        # mode to the user.
        if (len(sys.argv) < 2):
            self.args = self.parser.parse_args(args=['list'])
        else:
            self.args = self.parser.parse_args()

        '''Debug text below. Remove for release.'''
        if self.args.mode == 'log':
            print(f"self.args.amount='{self.args.amount}', self.args.name='{self.args.name}'")
        elif self.args.mode == 'rm':
            print(f'self.args.most_recent = {self.args.most_recent}')
        print(f'self.args.mode = {self.args.mode}')

        return self.args
