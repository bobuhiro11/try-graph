from __future__ import print_function
import argparse
import sys
import matplotlib
matplotlib.use('Agg')
# flake8: noqa
import matplotlib.pyplot as plt
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description='Try a graph')
    parser.add_argument('--input',
                        default=sys.stdin,
                        help='input filename')
    parser.add_argument('--ext',
                        default='png',
                        choices=['png', 'svg', 'ps', 'eps', 'pdf'],
                        help='output file extension')
    parser.add_argument('--xlabel',
                        default=None,
                        help='xlabel')
    parser.add_argument('--ylabel',
                        default=None,
                        help='ylabel')
    parser.add_argument('--title',
                        default=None,
                        help='title')
    parser.add_argument('--debug',
                        action='store_true',
                        help='print debug messages to stderr')
    parser.add_argument('--kind',
                        default='bar',
                        choices=['bar', 'hist', 'box', 'kde',
                                 'area', 'scatter', 'hexbin', 'pie'],
                        help='graph type')
    args = parser.parse_args()

    df = pd.read_csv(args.input, index_col=0)
    df.plot()

    if args.debug:
        print(df, file=sys.stderr)
    if args.xlabel is not None:
        plt.xlabel(args.xlabel)
    if args.ylabel is not None:
        plt.ylabel(args.ylabel)
    if args.title is not None:
        plt.title(args.title)

    plt.legend(bbox_to_anchor=(1.04, 0.5), loc="center left")
    outfile = sys.stdout.buffer if sys.version_info[0] >= 3 else sys.stdout
    plt.savefig(outfile, format=args.ext, bbox_inches="tight", dpi=200)


if __name__ == '__main__':
    main()
