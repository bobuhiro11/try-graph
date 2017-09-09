import argparse


def main():
    parser = argparse.ArgumentParser(description='Try a lot of graphs.')
    parser.add_argument('-f', '--filename',
                        default=None,
                        help='Input filename (Default: None).')
    parser.add_argument('-e', '--ext',
                        nargs='*',
                        help='Output file extension (Default: png svg).')
    args = parser.parse_args()

    print("main")
    print(args)


if __name__ == '__main__':
    main()
