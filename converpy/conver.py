#!/usr/bin/env python3
import argparse
import conversions as convert


input_function_map = {
    "milestokm": convert.miles_to_km,
    "kmtomiles": convert.km_to_miles,
    "kgtopounds": convert.kg_to_pounds,
    "poundstokg": convert.pounds_to_kg
}

parser = argparse.ArgumentParser(prog = "ConverPy")
parser.add_argument('operation', choices = input_function_map.keys(), type = str, help = "the conversion operation to be performed")
parser.add_argument('input', type = float, help = "value to be converted")

args = parser.parse_args()
operation = input_function_map[args.operation]

def main():
    return operation(args.input)

if __name__ == "__main__":
    print(main())
