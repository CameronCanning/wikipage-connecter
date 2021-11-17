import argparse
import linksearch

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("start_page", metavar='S', nargs=1,
                        help='start page name')
    parser.add_argument("end_page", metavar='E', nargs=1,
                        help='end page name')
    #parser.add_argument("max_depth", metavar='d', type=int, default=0, nargs='?',
#                        help='max depth of search')
    args = parser.parse_args()


    chain = linksearch.LinkSearch(args.start_page[0], args.end_page[0]).search()

    if chain:
        print('\nChain:')
        print(*chain, sep=" > ")


if __name__ == "__main__":
    main()
