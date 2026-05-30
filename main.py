import argparse

from weather import check_city

parser = argparse.ArgumentParser()

parser.add_argument("--city",type=str)

args = parser.parse_args()

if args.city:
    check_city(args.city)

