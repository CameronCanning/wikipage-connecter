import argparse
import pagereader
import linksearch

parser = argparse.ArgumentParser()
parser.add_argument("start_page", metavar='S', nargs=1,
                    help='start page name')
parser.add_argument("start_page", metavar='E', nargs=1,
                    help='end page name')
parser.add_argument("max_depth", metavar='d', type=int, nargs=1,
                    help='max depth of search', default=10)
args = parser.parse_args()
