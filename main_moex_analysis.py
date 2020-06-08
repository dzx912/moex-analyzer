#!/usr/bin/env python

import argparse
from moex_client import MoexClient


def main():
    parser = argparse.ArgumentParser(description='Analysis of Moscow Exchange Securities.')
    parser.add_argument('--security', help="Security for analysis")
    parser.add_argument('--date', help="Date of start analysis", default='1990-01-01')
    args = parser.parse_args()

    if args.security is not None:
        launch_client('stock', 'shares', 'TQBR', args.security, args.date)
    else:
        parser.print_help()


def launch_client(engine, market, board, security, date):
    client = MoexClient()
    data, column = client.get_history_securities(engine, market, board, security, date)
    if 0 < len(data):
        print(column)
        for item in data:
            print(item)
    else:
        print("We do not have any data.")
        print("Engine: {}, market: {}, board: {}, security: {}, date: {}"
              .format(engine, market, board, security, date))


if __name__ == '__main__':
    main()