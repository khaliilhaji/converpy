#!/usr/bin/env python3
import sys

input_err = "Incorrect input!!"

def check_type(x):
    if type(x) is int or type(x) is float:
        return True
    else:
        return False

def miles_to_km(miles):
    if check_type(miles):
        km = miles*1.60934
        return km
    else:
        return input_err

def km_to_miles(km):
    if check_type(km):
        miles = km/1.60934
        return km
    else:
        return input_err


def kg_to_pounds(kg):
    if check_type(kg):
        pounds = kg*2.2046226218
        return pounds
    else:
        return input_err

def pound_to_kg(pounds):
    if check_type(pounds):
        kg = pounds/2.2046226218
        return kg
    else:
        return input_err

def commandline():
    arguments = sys.argv
    result = []
    for x in range(1, len(arguments)):
        result.append(miles_to_km(float(arguments[x])))
    return result


if __name__ == '__main__':
    print(commandline())
