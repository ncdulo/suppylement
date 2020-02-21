import sys

import argparse


class Arguments():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                description='''
                Quick & easy to use nutritional supplement tracking software
                https://github.com/ncdulo/suppylement
                '''
            )
        # Should this be here, or in parse_args?
        self.subparsers = self.parser.add_subparsers(
                dest='mode',
                help='modes')

    def parse_args(self, args):
        # List mode
        self.list_parser = self.subparsers.add_parser(
                'list', help='list entries')
        self.list_parser.add_argument(
                '--most-recent',
                dest='most_recent',
                type=int,
                default=5,
                help='display MOST_RECENT entries, default 5')
        self.list_parser.add_argument(
                '--less',
                dest='search_less',
                type=int,
                default=-1,
                help='list entries where amount is less than SEARCH_LESS')
        self.list_parser.add_argument(
                '--more',
                dest='search_more',
                type=int,
                default=-1,
                help='list entries where amount is greater than SEARCH_MORE')
        self.list_parser.add_argument(
                '--name',
                dest='search_name',
                type=str,
                default='',
                help='list entries where name equals SEARCH_NAME')
        # Edit mode
        self.edit_parser = self.subparsers.add_parser(
                'edit', help='not yet implemented')
        self.edit_parser.add_argument(
                'id',
                type=int,
                help='id of entry to edit')
        # Log new entry mode
        self.log_parser = self.subparsers.add_parser(
                'log', help='log an entry')
        self.log_parser.add_argument(
                'amount',
                type=int,
                help='amount in miligrams')
        self.log_parser.add_argument(
                'name',
                type=str,
                help='name of supplement')
        # Remove entry mode
        self.rm_parser = self.subparsers.add_parser(
                'rm',
                help='remove specific entries')
        self.rm_parser.add_argument(
                '--id',
                dest='id_to_remove',
                type=int,
                default=-1,
                help='remove entry number ID_TO_REMOVE')
        self.rm_parser.add_argument(
                '-i',
                dest='rm_interactive',
                action='store_true',
                default=False,
                help='confirm before deleting row')
        self.rm_parser.add_argument(
                '--most-recent',
                dest='most_recent',
                type=int,
                default=1,
                help='remove MOST_RECENT entries')
        # Statistics mode
        self.stats_parser = self.subparsers.add_parser(
                'stats',
                help='display various statistics')
        self.stats_parser.add_argument(
                '--full',
                default=False,
                action='store_true',
                help='full output mode')

        self.args = self.parser.parse_args(args)

        #if self.args.mode == 'log':
        #    print(f"self.args.amount='{self.args.amount}', self.args.name='{self.args.name}'")
        #elif self.args.mode == 'rm':
        #    print(f'self.args.most_recent = {self.args.most_recent}')
        #print(f'self.args.mode = {self.args.mode}')

        return self.args
