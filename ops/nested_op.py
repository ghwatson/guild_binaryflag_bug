import argparse
import upstream_dep
parser = argparse.ArgumentParser()
parser.add_argument('--DEVMODE', action='store_true')


def main_with_args(args):
    print('hello world')
    print('flag:', args.DEVMODE)
    upstream_dep.goodbye()


if __name__ == '__main__':
    args = parser.parse_args()
    main_with_args(args)
