import argparse
import logging
from pyfiglet import figlet_format
from graphdetect.detector import Detector

logging.basicConfig(level=logging.INFO)
parser = argparse.ArgumentParser(description="GraphQL endpoint dectector")
parser.add_argument("url", type=str, help="To accept ")
parser.add_argument("--output",action='store',default=False, help='verify')
args = parser.parse_args()
url=args.url
print(figlet_format('GraphD', font='roman'))
print('\t\t\t\t\t\t\t\t By Udayon Sen\n')
dtector = Detector(url)
dtector.run()