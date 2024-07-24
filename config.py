from argparse import ArgumentParser, Namespace


parser: ArgumentParser = ArgumentParser()
parser.add_argument('driver_location')
parser.add_argument('-item', nargs=2, action='append', metavar=('PRODUCT_ID', 'DREAM_PRICE'))
args = parser.parse_args()
