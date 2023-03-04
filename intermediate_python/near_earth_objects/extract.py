"""Extract data on NEO and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about NEOs.
    :return: A collection of `NearEarthObject`s.
    """
    neo_list = []
    with open(neo_csv_path) as infile:
        csv_file = csv.reader(infile)
        next(csv_file)
        for row in csv_file:
            designation = row[3]
            name = row[4]
            hazardous = row[7]
            diameter = row[15]
            neo = {
                'designation': designation,
                'name': name,
                'hazardous': hazardous,
                'diameter': diameter,
            }
            neo_list.append(NearEarthObject(**neo))
    return neo_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close
    approaches.
    :return: A collection of `CloseApproach`es.
    """
    cad_list = []
    with open(cad_json_path) as infile:
        json_file = json.load(infile)
        for liste in json_file['data']:
            designation = liste[0]
            time = liste[3]
            distance = liste[4]
            velocity = liste[7]
            cad = {
                'designation': designation,
                'time': time,
                'distance': distance,
                'velocity': velocity
            }
            cad_list.append(CloseApproach(**cad))
    return cad_list
