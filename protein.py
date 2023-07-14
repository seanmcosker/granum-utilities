#import protein_utilities as pu
import argparse


parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument("new_data", help="New data to classify")

args = parser.parse_args()

new_data=args[0]

